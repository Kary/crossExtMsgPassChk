import MySQLdb
import random

# Kary
from config import mysqlInfo


# ----- selectExtDownloadByExtId -----
def selectExtDownloadByExtId(extId):
	dbConn = MySQLdb.connect(mysqlInfo['host'], mysqlInfo['user'], mysqlInfo['passwd'], mysqlInfo['db'])
	dbCursor = dbConn.cursor()
	selectSql = 'SELECT * FROM ExtDownload WHERE extId = %s;'
	values = (extId, )
	dbCursor.execute(selectSql, values)
	result = dbCursor.fetchall()
	return result
# ----- selectExtDownloadByExtId -----


# ----- selectExtDownloadByExtNum -----
def selectExtDownloadByExtNum(num):
	dbConn = MySQLdb.connect(mysqlInfo['host'], mysqlInfo['user'], mysqlInfo['passwd'], mysqlInfo['db'])
	dbCursor = dbConn.cursor()
	selectSql = 'SELECT * FROM ExtDownload WHERE num = %s;'
	values = (num, )
	dbCursor.execute(selectSql, values)
	result = dbCursor.fetchall()
	return result
# ----- selectExtDownloadByExtNum -----


# ----- selecJsResultByMd5 -----
def selecJsResultByMd5(md5):
	dbConn = MySQLdb.connect(mysqlInfo['host'], mysqlInfo['user'], mysqlInfo['passwd'], mysqlInfo['db'])
	dbCursor = dbConn.cursor()
	selectSql = 'SELECT * FROM JsResult WHERE md5 = %s LIMIT %s;'
	values = (md5, 1)
	dbCursor.execute(selectSql, values)
	result = dbCursor.fetchall()
	return result
# ----- selectExtEsprimaByMd5 -----


# ----- selectJsResultByExtName -----
def selectJsResultByExtName(extFolderName):
	dbConn = MySQLdb.connect(mysqlInfo['host'], mysqlInfo['user'], mysqlInfo['passwd'], mysqlInfo['db'])
	dbCursor = dbConn.cursor()
	selectSql = 'SELECT * FROM JsResult WHERE extFolderName = %s;'
	values = (extFolderName, )
	dbCursor.execute(selectSql, values)
	result = dbCursor.fetchall()
	return result
# ----- selectJsResultByExtName -----


# ----- selectDupJsResultByExtName -----
def selectDupJsResultByExtName(extFolderName):
	dbConn = MySQLdb.connect(mysqlInfo['host'], mysqlInfo['user'], mysqlInfo['passwd'], mysqlInfo['db'])
	dbCursor = dbConn.cursor()
	selectSql = 'SELECT * FROM JsResult WHERE extFolderName = %s AND sExtFolderName != %s AND extFolderName != sExtFolderName;'
	values = (extFolderName, '')
	dbCursor.execute(selectSql, values)
	result = dbCursor.fetchall()
	return result
# ----- selectDupJsResultByExtName -----


# ----- selectNotEsprimaJsResult -----
def selectNotEsprimaJsResult(extFolderName):
	dbConn = MySQLdb.connect(mysqlInfo['host'], mysqlInfo['user'], mysqlInfo['passwd'], mysqlInfo['db'])
	dbCursor = dbConn.cursor()
	selectSql = 'SELECT js FROM JsResult WHERE extFolderName = %s AND esprima = %s;'
	values = (extFolderName, 'N')
	dbCursor.execute(selectSql, values)
	result = dbCursor.fetchall()
	return result
# ----- selectNotEsprimaJsResult -----


# ----- selectExtForManualAnalysis -----
def selectExtForManualAnalysis():
	dbConn = MySQLdb.connect(mysqlInfo['host'], mysqlInfo['user'], mysqlInfo['passwd'], mysqlInfo['db'])
	dbCursor = dbConn.cursor()
	selectSql = 'SELECT extFolderName FROM ExtResult WHERE manualCheck = %s;'
	values = ('U', )
	dbCursor.execute(selectSql, values)
	result = dbCursor.fetchall()
	return result
# ----- select10ExtForManualAnalysis -----


# ----- randomExtForManualAnalysis -----
def randomExtForManualAnalysis(num):
	dbResult = selectExtForManualAnalysis()
	allNum = list(range(0, len(dbResult)))
	random.shuffle(allNum)
	
	extFolderNames = []
	for i in range(0, num):
		extFolderNames.append(dbResult[allNum[i]][0])
	return extFolderNames
# ----- randomExtForManualAnalysis -----


# ----- numExtForManualAnalysis -----
def numExtForManualAnalysis():
	dbConn = MySQLdb.connect(mysqlInfo['host'], mysqlInfo['user'], mysqlInfo['passwd'], mysqlInfo['db'])
	dbCursor = dbConn.cursor()
	selectSql = 'SELECT COUNT(extFolderName) FROM ExtResult WHERE manualCheck = %s;'
	values = ('U', )
	dbCursor.execute(selectSql, values)
	result = dbCursor.fetchall()
	return result
# ----- numExtForManualAnalysis -----


# ----- selectAssignTableByExtId -----
def selectAssignTableByExtId(extId):
	dbConn = MySQLdb.connect(mysqlInfo['host'], mysqlInfo['user'], mysqlInfo['passwd'], mysqlInfo['db'])
	dbCursor = dbConn.cursor()
	selectSql = 'SELECT * FROM JsContent WHERE extFolderName LIKE %s AND tableType = %s;'
	values = ('%' + extId, 'A')
	dbCursor.execute(selectSql, values)
	result = dbCursor.fetchall()
	return result
# ----- selectAssignTableByExtId -----


# ----- selectAssignTableByExtNum -----
def selectAssignTableByExtNum(num):
	dbConn = MySQLdb.connect(mysqlInfo['host'], mysqlInfo['user'], mysqlInfo['passwd'], mysqlInfo['db'])
	dbCursor = dbConn.cursor()
	selectSql = 'SELECT * FROM JsContent WHERE extFolderName LIKE %s AND tableType = %s;'
	values = (num.zfill(6) + '%', 'A')
	dbCursor.execute(selectSql, values)
	result = dbCursor.fetchall()
	return result
# ----- selectAssignTableByExtNum -----


# ----- selectCallTableByExtId -----
def selectCallTableByExtId(extId):
	dbConn = MySQLdb.connect(mysqlInfo['host'], mysqlInfo['user'], mysqlInfo['passwd'], mysqlInfo['db'])
	dbCursor = dbConn.cursor()
	selectSql = 'SELECT * FROM JsContent WHERE extFolderName LIKE %s AND tableType = %s;'
	values = ('%' + extId, 'C')
	dbCursor.execute(selectSql, values)
	result = dbCursor.fetchall()
	return result
# ----- selectCallTableByExtId -----


# ----- selectCallTableByExtNum -----
def selectCallTableByExtNum(num):
	dbConn = MySQLdb.connect(mysqlInfo['host'], mysqlInfo['user'], mysqlInfo['passwd'], mysqlInfo['db'])
	dbCursor = dbConn.cursor()
	selectSql = 'SELECT * FROM JsContent WHERE extFolderName LIKE %s AND tableType = %s;'
	values = (num.zfill(6) + '%', 'C')
	dbCursor.execute(selectSql, values)
	result = dbCursor.fetchall()
	return result
# ----- selectCallTableByExtNum -----


# ----- selectJsResultByExtId -----
def selectJsResultByExtId(extId):
	dbConn = MySQLdb.connect(mysqlInfo['host'], mysqlInfo['user'], mysqlInfo['passwd'], mysqlInfo['db'])
	dbCursor = dbConn.cursor()
	selectSql = 'SELECT * FROM JsResult WHERE extFolderName LIKE %s;'
	values = ('%' + extId, )
	dbCursor.execute(selectSql, values)
	result = dbCursor.fetchall()
	return result
# ----- selectJsResultByExtId -----


# ----- selectJsResultByExtNum -----
def selectJsResultByExtNum(num):
	dbConn = MySQLdb.connect(mysqlInfo['host'], mysqlInfo['user'], mysqlInfo['passwd'], mysqlInfo['db'])
	dbCursor = dbConn.cursor()
	selectSql = 'SELECT * FROM JsResult WHERE extFolderName LIKE %s;'
	values = (num.zfill(6) + '%', )
	dbCursor.execute(selectSql, values)
	result = dbCursor.fetchall()
	return result
# ----- selectJsResultByExtNum -----


# ----- selectExtResultByExtId -----
def selectExtResultByExtId(extId):
	dbConn = MySQLdb.connect(mysqlInfo['host'], mysqlInfo['user'], mysqlInfo['passwd'], mysqlInfo['db'])
	dbCursor = dbConn.cursor()
	selectSql = 'SELECT * FROM ExtResult WHERE extFolderName LIKE %s;'
	values = ('%' + extId, )
	dbCursor.execute(selectSql, values)
	result = dbCursor.fetchall()
	return result
# ----- selectExtResultByExtId -----


# ----- selectExtResultByExtNum -----
def selectExtResultByExtNum(num):
	dbConn = MySQLdb.connect(mysqlInfo['host'], mysqlInfo['user'], mysqlInfo['passwd'], mysqlInfo['db'])
	dbCursor = dbConn.cursor()
	selectSql = 'SELECT * FROM ExtResult WHERE extFolderName LIKE %s;'
	values = (num.zfill(6) + '%', )
	dbCursor.execute(selectSql, values)
	result = dbCursor.fetchall()
	return result
# ----- selectExtResultByExtNum -----

# ----- selectHtmlResultByExtId -----
def selectHtmlResultByExtId(extId):
	dbConn = MySQLdb.connect(mysqlInfo['host'], mysqlInfo['user'], mysqlInfo['passwd'], mysqlInfo['db'])
	dbCursor = dbConn.cursor()
	selectSql = 'SELECT * FROM HtmlResult WHERE extFolderName LIKE %s;'
	values = ('%' + extId, )
	dbCursor.execute(selectSql, values)
	result = dbCursor.fetchall()
	return result
# ----- selectHtmlResultByExtId -----


# ----- selectHtmlResultByExtNum -----
def selectHtmlResultByExtNum(num):
	dbConn = MySQLdb.connect(mysqlInfo['host'], mysqlInfo['user'], mysqlInfo['passwd'], mysqlInfo['db'])
	dbCursor = dbConn.cursor()
	selectSql = 'SELECT * FROM HtmlResult WHERE extFolderName LIKE %s;'
	values = (num.zfill(6) + '%', )
	dbCursor.execute(selectSql, values)
	result = dbCursor.fetchall()
	return result
# ----- selectHtmlResultByExtNum -----