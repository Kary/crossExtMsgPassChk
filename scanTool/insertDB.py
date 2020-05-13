import MySQLdb


# Kary
from config import mysqlInfo


# ----- getLoc -----
def getLoc(s):
	return (s.split(',')[0].split('line: ')[-1].strip(), 
		s.split(',')[1].split('column: ')[-1].replace('}', '').strip(), 
		s.split(',')[2].split('line: ')[-1].strip(), 
		s.split(',')[-1].split('column: ')[-1].replace('}', '').strip())
# ----- getLoc -----


# ----- insertJsResult -----
def insertJsResult(extFolderName, js, md5, sExtFolderName, sJs, esprima, duplicate, ec, cs, dev):
	dbConn = MySQLdb.connect(mysqlInfo['host'], mysqlInfo['user'], mysqlInfo['passwd'], mysqlInfo['db'])
	dbCursor = dbConn.cursor()
	insertSql = 'INSERT INTO JsResult (extFolderName, js, md5, sExtFolderName, sJs, esprima, duplicate, ec, cs, dev) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
	values = (extFolderName, js, md5, sExtFolderName, sJs, esprima, duplicate, ec, cs, dev)
	dbCursor.execute(insertSql, values)
	dbConn.commit()
# ----- insertJsResult -----

# ----- insertJsContent -----
def insertJsContent(extFolderName, table, tableType):
	dbConn = MySQLdb.connect(mysqlInfo['host'], mysqlInfo['user'], mysqlInfo['passwd'], mysqlInfo['db'])
	dbCursor = dbConn.cursor()
	for t in table:
		sLine, sCol, eLine, eCol = getLoc(str(t[2]))
		insertSql = 'INSERT INTO JsContent (extFolderName, js, tableType, jsKey, jsValue, sLine, sCol, eLine, eCol) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);'
		values = (extFolderName, str(t[3]), tableType, str(t[0])[0:500], str(t[1])[0:500], sLine, sCol, eLine, eCol)
		dbCursor.execute(insertSql, values)
		dbConn.commit()
# ----- insertJsContent -----

# ----- insertHtmlResult -----
def insertHtmlResult(extFolderName, html, ec, cs, dev):
	dbConn = MySQLdb.connect(mysqlInfo['host'], mysqlInfo['user'], mysqlInfo['passwd'], mysqlInfo['db'])
	dbCursor = dbConn.cursor()
	insertSql = 'INSERT INTO HtmlResult (extFolderName, html, ec, cs, dev) VALUES (%s, %s, %s, %s, %s);'
	values = (extFolderName, html, ec, cs, dev)
	dbCursor.execute(insertSql, values)
	dbConn.commit()
# ----- insertHtmlResult -----

# ----- insertExtResult -----
def insertExtResult(extFolderName, ecInlineScript, devInlineScript, staticCheck, manualCheck, comment):
	dbConn = MySQLdb.connect(mysqlInfo['host'], mysqlInfo['user'], mysqlInfo['passwd'], mysqlInfo['db'])
	dbCursor = dbConn.cursor()
	insertSql = 'INSERT INTO ExtResult (extFolderName, ecInlineScript, devInlineScript, staticCheck, manualCheck, comment) VALUES (%s, %s, %s, %s, %s, %s);'
	values = (extFolderName, ecInlineScript, devInlineScript, staticCheck, manualCheck, comment)
	dbCursor.execute(insertSql, values)
	dbConn.commit()
# ----- insertExtResult -----