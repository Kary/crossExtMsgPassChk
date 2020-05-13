import MySQLdb


# Kary
from config import mysqlInfo


# ----- updateJsResultDuplicate -----
def updateJsResultDuplicate(extFolderName):
	dbConn = MySQLdb.connect(mysqlInfo['host'], mysqlInfo['user'], mysqlInfo['passwd'], mysqlInfo['db'])
	dbCursor = dbConn.cursor()
	updateSql = 'UPDATE JsResult SET duplicate = %s WHERE extFolderName = %s;'
	values = (1, extFolderName)
	dbCursor.execute(updateSql, values)
	dbConn.commit()
# ----- updateJsResultDuplicate -----


# ----- updateJsResultComponents -----
def updateJsResultComponents(extFolderName, js, ec, cs, dev, esprima):
	if ec != 0 or cs != 0 or dev != 0:
		dbConn = MySQLdb.connect(mysqlInfo['host'], mysqlInfo['user'], mysqlInfo['passwd'], mysqlInfo['db'])
		dbCursor = dbConn.cursor()
		updateSql = 'UPDATE JsResult SET ec = %s, cs = %s, dev = %s, esprima = %s WHERE extFolderName = %s AND js = %s;'
		values = (ec, cs, dev, esprima, extFolderName, js)
		dbCursor.execute(updateSql, values)
		dbConn.commit()
# ----- updateJsResultComponents -----


# ----- updateExtResultByExtId -----
def updateExtResultByExtId(extId, result, comment):
	dbConn = MySQLdb.connect(mysqlInfo['host'], mysqlInfo['user'], mysqlInfo['passwd'], mysqlInfo['db'])
	dbCursor = dbConn.cursor()
	updateSql = 'UPDATE ExtResult SET manualCheck = %s, comment = %s WHERE extFolderName LIKE %s;'
	values = (result, comment, '%' + extId)
	dbCursor.execute(updateSql, values)
	dbConn.commit()
# ----- updateExtResultByExtId -----

# ----- updateExtResultByExtNum -----
def updateExtResultByExtNum(num, result, comment):
	dbConn = MySQLdb.connect(mysqlInfo['host'], mysqlInfo['user'], mysqlInfo['passwd'], mysqlInfo['db'])
	dbCursor = dbConn.cursor()
	updateSql = 'UPDATE ExtResult SET manualCheck = %s, comment = %s WHERE extFolderName LIKE %s;'
	values = (result, comment, num.zfill(6) + '%')
	dbCursor.execute(updateSql, values)
	dbConn.commit()
# ----- updateExtResultByExtNum -----