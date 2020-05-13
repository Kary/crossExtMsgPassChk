import sys, os, shutil
from termcolor import colored
import hashlib
from functools import partial
import math
import mmap, contextlib
import re


# ----- Color -----
def grey(s): return colored(s, 'grey')
def red(s): return colored(s, 'red')
def green(s): return colored(s, 'green')
def yellow(s): return colored(s, 'yellow')
def blue(s): return colored(s, 'blue')
def magenta(s): return colored(s, 'magenta')
def cyan(s): return colored(s, 'cyan')
def white(s): return colored(s, 'white')
# ----- Color -----


# ----- printEsprimaError -----
def printEsprimaError():
	print('Esprima Error')
# ----- printEsprimaError -----


# ----- printDupExt -----
def printDupExt():
	print('Similar Ext')
# ----- printDupExt -----


# ----- printNoCrossExtMsg -----
def printNoCrossExtMsg():
	print('Not Cross-Ext Msg Sender')
# ----- printNoCrossExtMsg -----


# ----- printManualCheck -----
def printManualCheck():
	print(cyan('Manual Check'))
# ----- printManualCheck -----


# ----- Search4Keyword ----- Manual Analysis
def Search4Keyword(extFolder, keyword):
	found = False
	for root, dirs, files in os.walk(extFolder, topdown = False):
		for f in files:
			if f.endswith('.js'):
				jsPath = os.path.join(root, f)
				if os.stat(jsPath).st_size != 0:
					jsb = open(jsPath, 'rb', 0)
					with contextlib.closing(mmap.mmap(jsb.fileno(), 0, access = mmap.ACCESS_READ)) as s:
						if re.search(keyword.encode(), s):
							ver = jsPath.split(extFolder + '/')[-1].split('/')[0]
							print(jsPath.split(extFolder + '/' + ver + '/')[-1])
							found = True
					jsb.close()
	return found
# ----- Search4Keyword -----


# ----- getNumFolder -----
def getNumFolder(num):
	return str((math.floor(num / 10000) + 1) * 10000).zfill(6)
# ----- getNumFolder -----


# ----- getStartNumEndNum -----
def getStartNumEndNum():
	if len(sys.argv) == 3: 
		if int(sys.argv[2]) >= int(sys.argv[1]):
			return int(sys.argv[1]), int(sys.argv[2])
	printUsage()
# ----- getStartNumEndNum -----


# ----- colorForPrintResult -----
def colorForPrintResult(text, index):
	if index == 0:
		return text
	elif index%2 == 0:
		return text
	else:
		return green(text)
# ----- colorForPrintResult -----


# ----- printResult -----
def printResult(sectionText, fileList):
	print(yellow(sectionText))
	for f in range(0, len(fileList)):
		print(colorForPrintResult(fileList[f], f), end = ' ') 
	print('')
# ----- printResult -----


# ----- printDupResult -----
def printDupResult(sectionText, fileList):
	print(cyan(sectionText))
	for f in range(0, len(fileList)):
		print(colorForPrintResult(fileList[f], f), end = ' ') 
	print('')
# ----- printDupResult -----


# ----- printUsage -----
def printUsage():
	print('Usage:', yellow('python3 XXX.py <startNum> <endNum>'))
	print('Check for extensions between <startNum> and <endNum>')
	print('Example: python3 XXX.py 1 10000')
	sys.exit()
# ----- printUsage -----


# ----- createFolder -----
def createFolder(d):
	if not os.path.exists(d):
		os.makedirs(d)
# ----- createFolder -----


# ----- removeFolder -----
def removeFolder(d):
	if os.path.exists(d):
		shutil.rmtree(d)
# ----- removeFolder -----


# ----- removeFile -----
def removeFile(f):
	if os.path.exists(f):
		os.remove(f)
# ----- removeFile -----


# ----- writeError -----
def writeError(error, info, newExtFolder):
	staticChkResult = open(newExtFolder + '/' + 'staticChkResult.txt', 'a+')
	staticChkResult.write(error + ': ' + info  + '\n')
	staticChkResult.close()
	print(red(error), info)
# ----- writeError -----


# ----- getScriptTypeForFilesFromTable ----- return list contains ec, cs or/and dev
def getFilesScriptTypeFromTable(table, file):
	scriptTypes = []
	for s in table:
		if s[0] == file:
			if s[1] == 1:
				scriptTypes.append('ec')
			elif s[2] == 1:
				scriptTypes.append('cs')
			elif s[3] == 1:
				scriptTypes.append('dev')
	return scriptTypes
# ----- getFilesScriptTypeFromTable -----


# ----- writeTable -----
def writeTable(table):
	# 3 Js
	ecScripts, csScripts, devScripts = [], [], []
	unusedScripts = []
	
	# scriptType: ec, cs, dev
	for s in table:
		if s[1] == 1:
			ecScripts.append(s[0])
		elif s[2] == 1:
			csScripts.append(s[0])
		elif s[3] == 1:
			devScripts.append(s[0])
		else:
			unusedScripts.append(s[0])

	if len(ecScripts) > 0:
		print(blue('Extension Core'), ecScripts)

	if len(csScripts) > 0:
		print(blue('Content Scripts'), csScripts)

	if len(devScripts) > 0:
		print(blue('Dev'), devScripts)

	if len(unusedScripts) > 0:
		print(yellow('Unused'), unusedScripts) 
# ----- writeTable -----


# ----- notYetProcessedJs -----
def notYetProcessedJs(table):
	for s in table:
		if s[1] + s[2] + s[3] > 0 and s[4] == 0:
			return True
	return False
# ----- notYetProcessedJs -----

# ----- getRowNoInTable -----
def getRowNoInTable(table, file):
	for i in range(0, len(table)):
		if table[i][0] == file:
			return i
# ----- getRowNoInTable -----


# ----- updateTable ----- when js or hrml file belongs to that component
def updateTable(table, file, scriptType):
	components = ['ec', 'cs', 'dev']
	for s in table:
		for i in range(0, len(components)):
			if s[0] == file: # s[0] filename
				if scriptType == components[i]:
					s[i+1] = 1
	return table
# ----- updateTable -----


# ----- updateTableForJs -----
def updateTableForJs(table, orgFile, newFile):
	oriRow = 0
	newRow = 0

	for i in range(0, len(table)): # Get Row No. of Original Js and New Js
		if table[i][0] == orgFile:
			oriRow = i
		elif table[i][0] == newFile:
			newRow = i

	for j in range(1, 4): # Update
		if table[oriRow][j] == 1:
			table[newRow][j] = 1			

	return table
# ----- updateTableForJs -----


# ----- updateTableForHtml -----
def updateTableForHtml(jsTable, htmlTable, js, html):
	scriptTypes = getFilesScriptTypeFromTable(jsTable, js)
	for s in scriptTypes:
		htmlTable = updateTable(htmlTable, html, s)
	return htmlTable
# ----- updateTableForHtml -----


# ----- getJsKeywordsfromTable -----
def getJsKeywordsfromTable(table):
	keywords = []
	for s in table:
		k = s[0].split('/')[-1].rstrip('.js') 
		if k not in keywords:
			keywords.append(k)
	return keywords
# ----- getJsKeywordsfromTable -----


# ----- getHtmlKeywordsfromTable -----
def getHtmlKeywordsfromTable(table):
	keywords = []
	for s in table:
		k = s[0].split('/')[-1].rstrip('.html') 
		if k not in keywords:
			keywords.append(k)
	return keywords
# ----- getHtmlKeywordsfromTable -----


# ----- genMd5 -----
def genMd5(f):
	d = hashlib.md5()
	for b in iter(partial(f.read, 128), b''):
		d.update(b)
	return d.hexdigest()
# ----- genMd5 -----