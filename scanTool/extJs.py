import os
import esprima
import subprocess
import re
import mmap, contextlib


# Kary
import commonCode
from esprimaVisitor import esprimaVisitor
# import selectDB, updateDB
import extHtml


# ----- getAllJSs -----
# allJSs have been extracted from 1) manifest file & 2) html file
# Now extract from Js Files
def getAllJSs(extFolderName, allJSs, allHtmls, ecInlineScript, devInlineScript, verFolder, newVerFolder, assignTable, callTable):
	extId = extFolderName.split('_')[-1]

	for x in range(0, len(allJSs)): 
		if allJSs[x][1] + allJSs[x][2] + allJSs[x][3] > 0 and allJSs[x][4] == 0: # js, ec, cs, dev, processed, esprima
			allJSs[x][4] = 1
			js = allJSs[x][0]
			# beautifierJs
			newJsPath = beautifierJs(js, verFolder, newVerFolder)

			try:
				newJsFile = open(newJsPath, 'r', encoding = 'utf-8')
				newJsData = newJsFile.read()
				newJsFile.close()
				
			except UnicodeDecodeError as e:
				newJsFile = open(newJsPath, 'r', encoding = 'ISO-8859-1')
				newJsData = newJsFile.read()
				newJsFile.close()

			
			# esprima
			try:
				# print(js)
				jsKeywords = commonCode.getJsKeywordsfromTable(allJSs)
				htmlKeywords = commonCode.getHtmlKeywordsfromTable(allHtmls)

				newJsVisitor = esprimaVisitor(extId, js, htmlKeywords, jsKeywords)
				newJsTree = esprima.parse(newJsData, {'loc': True}, delegate = newJsVisitor)
				newJsVisitor.visit(newJsTree)

				# jsParse = esprima.parseScript(js.read(), {'loc': True})
				# txt = open('esprimaOutput.txt', 'a+')
				# txt.write(str(jsParse))
				# txt.close()

				literalTable = newJsVisitor.returnLiteralTable()

				jsPath = verFolder + '/' + js
				jsFolder = os.path.dirname(jsPath)

				# Get JS
				for l in literalTable:
					for j in jsKeywords:
						if j in l:
							i = l
							if not l.endswith('.js'):
								i = i + '.js'

							if os.path.exists(jsFolder + '/' + i):
								if os.stat(jsFolder + '/' + i).st_size != 0:
									oJs = os.path.normpath(jsFolder + '/' + i).split(verFolder + '/')[-1]
									allJSs = commonCode.updateTableForJs(allJSs, js, oJs)

							elif os.path.exists(verFolder + '/' + i):
								if os.stat(verFolder + '/' + i).st_size != 0:
									oJs = os.path.normpath(verFolder + '/' + i).split(verFolder + '/')[-1]
									allJSs = commonCode.updateTableForJs(allJSs, js, oJs)

					for h in htmlKeywords:
						if h in l:
							if l.endswith('.html'):
								if os.path.exists(jsFolder + '/' + l):
									if os.stat(jsFolder + '/' + l).st_size != 0:
										oHtml = os.path.normpath(jsFolder + '/' + l).split(verFolder + '/')[-1]

										allHtmls = commonCode.updateTableForHtml(allJSs, allHtmls, js, oHtml)
										rowNo = commonCode.getRowNoInTable(allHtmls, oHtml)
										if allHtmls[rowNo][4] == 0:
											allHtmls[rowNo][4] = 1
											allJSs, ecInlineScript, devInlineScript = extHtml.getJSsForEachHtml(oHtml, verFolder, allJSs, allHtmls, ecInlineScript, devInlineScript)

								elif os.path.exists(verFolder + '/' + l):
									if os.stat(verFolder + '/' + l).st_size != 0:
										oHtml = os.path.normpath(verFolder + '/' + l).split(verFolder + '/')[-1]
										
										allHtmls = commonCode.updateTableForHtml(allJSs, allHtmls, js, oHtml)
										rowNo = commonCode.getRowNoInTable(allHtmls, oHtml)

										if allHtmls[rowNo][4] == 0:
											allHtmls[rowNo][4] = 1
											allJSs, ecInlineScript, devInlineScript = extHtml.getJSsForEachHtml(oHtml, verFolder, allJSs, allHtmls, ecInlineScript, devInlineScript)

				assignTable = assignTable + newJsVisitor.returnAssignTable()
				callTable = callTable + newJsVisitor.returnCallTable()

			except (esprima.error_handler.Error, RecursionError) as e:
				allJSs[x][5] = 0

	if commonCode.notYetProcessedJs(allJSs):
		allJSs, allHtmls, ecInlineScript, devInlineScript, assignTable, callTable = getAllJSs(extFolderName, allJSs, allHtmls, ecInlineScript, devInlineScript, verFolder, newVerFolder, assignTable, callTable)

	return allJSs, allHtmls, ecInlineScript, devInlineScript, assignTable, callTable
# ----- getAllJSs -----


# ----- beautifierJs -----
def	beautifierJs(js, verFolder, newVerFolder):
	beautifierOutput = subprocess.run(['js-beautify', verFolder + '/' + js], stdout=subprocess.PIPE)
	newJsPath = newVerFolder + '/' + js

	commonCode.createFolder(os.path.dirname(newJsPath))

	commonCode.removeFile(newJsPath)
	newJsFile = open(newJsPath, 'a+')
	newJsFile.write(str(beautifierOutput.stdout.decode()))
	newJsFile.close()

	return newJsPath
# ----- beautifierJs -----

# ----- writeInlineScriptToFile -----
def writeInlineScriptToFile(inlineScript, newVerFolder, scriptType):
	fileName = ''

	if scriptType == 'ec':
		fileName = 'ecInlineScript.js'
	elif scriptType == 'dev':
		fileName = 'devInineScript.js'

	newJsPath = newVerFolder + '/' + fileName
	newJsFile = open(newJsPath, 'a+')
	newJsFile.write(inlineScript)
	newJsFile.close()

	return fileName
# ----- writeInlineScriptToFile -----
