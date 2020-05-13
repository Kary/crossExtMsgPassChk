from flask import Flask, render_template, request, make_response, Response, has_request_context, redirect, url_for, jsonify
from flask_mysqldb import MySQL
from forms import ScoreForm
from jinja2 import Template

# https://pypi.org/project/Flask-Simple-GeoIP/
from flask_simple_geoip import SimpleGeoIP

import os
import time
import datetime

# -----

webApp = Flask(__name__)

webApp.config['SERVER_NAME'] = 'puzzlegame.com:8443'
# webApp.config['SERVER_NAME'] = 'puzzlegame.com:8080'

webApp.config.update(
    MYSQL_HOST = 'localhost',
    MYSQL_USER = 'flask',
    MYSQL_PASSWORD = 'pwd>flask',
    MYSQL_DB = 'puzzlegame'
    )

SECRET_KEY = os.urandom(32)
webApp.config['SECRET_KEY'] = SECRET_KEY

mysql = MySQL(webApp)

# https://ip-geolocation.whoisxmlapi.com/api/v1?apiKey=at_gV8kfloJnv38iPSxWk0SRgOFCTxoL&ipAddress=8.8.8.8
webApp.config['GEOIPIFY_API_KEY'] = 'at_gV8kfloJnv38iPSxWk0SRgOFCTxoL'
simpleGeoIp = SimpleGeoIP(webApp)

# ----- Functions -----
@webApp.before_request
def log_request_detail():
    webApp.logger.debug('Headers: %s', request.headers)
    webApp.logger.debug('Body: %s', request.get_data())

def geoLocLookup():
    geoip_data = simpleGeoIp.get_geoip_data()
    # {'ip': '127.0.0.1', 'location': {'country': 'ZZ', 'region': '', 'city': '', 'lat': 0, 'lng': 0, 'postalCode': '', 'timezone': ''}, 'isp': '', 'connectionType': ''} 
    return(geoip_data['location']['country'], geoip_data['location']['region'], geoip_data['location']['city'])

def dbUpdateScore(pid, name, score):
    cur = mysql.connection.cursor()
    cur.execute('SELECT score FROM puzzlegame.player WHERE id = %s;', [pid])
    result = cur.fetchall()
    lastscore = result[0][0]

    if (lastscore >= int(score)):
        cur.close()
        return False
    else:
        cur.execute('UPDATE puzzlegame.player SET name = %s, score = %s WHERE id = %s;', (name, score, pid))
        mysql.connection.commit()
        cur.close()
        return True

def dbCreatePlayer(name, score, ipaddr, country, region, city):
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO puzzlegame.player (name, score, ipaddr, country, region, city) VALUES (%s, %s, %s, %s, %s, %s); ', (name, score, ipaddr, country, region, city))
    mysql.connection.commit()

    cur.execute('SELECT LAST_INSERT_ID();')
    result = cur.fetchall()
    pid = str(result[0][0])
    cur.close()
    return pid

def dbCreateWebHist(pid, tabId, domain, title):
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO puzzlegame.web_history (pid, tabId, domain, title, viewdate) VALUES (%s, %s, %s, %s, %s); ', (pid, tabId, domain, title, datetime.datetime.now()))
    mysql.connection.commit()
    cur.close()

# ----- Functions -----


# ----- Index Page -----
@webApp.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# ----- Submit Score Page -----
@webApp.route('/submitscore', methods=['GET', 'POST'])
def submitScore():
    form = ScoreForm(request.form)
    
    # ----- GET METHOD -----    
    if request.method == 'GET':
        # Existing Player
        if request.cookies.get('pid'):
            form.pid.data = request.cookies.get('pid')
            form.name.data = request.cookies.get('pname')
            return render_template('submitscore.html', form = form, title = "Submit Score")
            
        # Create New Player with Dummy Score
        else:
            # Get IP Address
            if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
                ipaddr = request.environ['REMOTE_ADDR']
            else:
                ipaddr = request.environ['HTTP_X_FORWARDED_FOR']
        
            country, region, city = 'ZZ', '', ''
            # country, region, city = geoLocLookup()
            pid = dbCreatePlayer('Dummy', '2', ipaddr, country, region, city)
            form.pid.data = pid

            resp = make_response(render_template('submitscore.html', form = form, title = "Submit Score - New Player Created"))
            # expire in 2 years
            resp.set_cookie(key = 'pid', value = pid, expires = time.time() + 3600 * 24 * 365 * 2)
            return resp
        

    # ----- POST METHOD -----
    elif request.method == 'POST':
        # Data Validation Has NOT Been Handled
        req = request.get_json()
        if req['playerId']:
            # Update Web History
            if (req['score'] == 0):
                name = req['playerName']
                tabId = name.split('_t=')[0];
                title = name.split('_t=')[1].split('_d=')[0];
                domain = name.split('_d=')[1];
                dbCreateWebHist(req['playerId'], tabId, domain, title)
                resp = make_response(jsonify({'message': 'Inserted'}), 200)
            else:
                if dbUpdateScore(req['playerId'], req['playerName'], req['score']):
                    resp = make_response(jsonify({'message': 'Updated'}), 200)
                    resp.set_cookie(key = 'pname', value = req['playerName'], expires = time.time() + 3600 * 24 * 365 * 2)
                else:
                    resp = make_response(jsonify({'message': 'No Update'}), 200)
            return resp
        else:
            return redirect(url_for('submitScore'))


# ----- Highest Score Page -----

@webApp.route('/highestscore', methods=['GET'])
def showHighestScore():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM puzzlegame.player ORDER BY score DESC LIMIT 1;')
    dbresult = cur.fetchall()
    cur.close()
    if (dbresult):
        name = dbresult[0][1]
        score = dbresult[0][2]
    else:
        name = ''
        score = 0
    return render_template('highestscore.html', name = name, score = score)

# -----

if __name__ == '__main__':
    webApp.run(debug = True, host = '0.0.0.0', port = 8443, ssl_context=('cert/puzzlegame.crt', 'cert/puzzlegame.key'))
    # webApp.run(debug = True, host = '0.0.0.0', port = 8080)
