import os

# Kary
import commonCode
import extManifest, extHtml, extJs
import selectDB, insertDB, updateDB
from config import parentFolder


# ----- main -----
def main():
	
	startNum, endNum = commonCode.getStartNumEndNum()

	num = commonCode.getNumFolder(startNum)

	# Create Folder
	newNum = num + '_Update'
	numFolder = parentFolder + '/' + num
	newNumFolder = parentFolder + '/' + newNum
	commonCode.createFolder(newNumFolder)

	for extFolderName in os.listdir(numFolder):
		extFolder = numFolder + '/' + extFolderName

		if os.path.isdir(extFolder):
			seq = int(extFolderName.split('_')[0].lstrip())

			if startNum <= seq <= endNum:
				print(commonCode.yellow(seq), '/', endNum)
				
				extId = extFolderName.split('_')[-1]
				extDlRecord = selectDB.selectExtDownloadByExtId(extId)

				if len(extDlRecord) > 0:
					if extDlRecord[0][2] == 1: # dl
						verNo = extDlRecord[0][3]
						# url = extDlRecord[0][5]
						verFolder = extFolder + '/' + verNo

						# Js
						allJSs, allHtmls = [], []

						# Init: Get All JSs & Htmls					
						for root, dirs, files in os.walk(extFolder, topdown = False):
							for f in files:								
								if f.endswith('.js'):
									jsPath = os.path.join(root, f)
									if os.stat(jsPath).st_size != 0:
										js = jsPath.split(verFolder + '/')[-1]
										allJSs.append([js, 0, 0, 0, 0, 1]) # ec, cs, dev, processed, esprima

										# Kary: Commented for Re-scan
										jsb = open(jsPath, 'rb', 0)
										md5 = commonCode.genMd5(jsb)
										jsb.close()
										
										extEsprimaRecords = selectDB.selecJsResultByMd5(md5)
										if len(extEsprimaRecords) > 0:
											sExtFolderName = extEsprimaRecords[0][1]
											sJs = extEsprimaRecords[0][2]
											insertDB.insertJsResult(extFolderName, js, md5, sExtFolderName, sJs, 'U', 0, 0, 0, 0)
										else:
											# extFolderName, js, md5, sExtFolderName, sJs, esprima, duplicate, ec, cs, dev
											insertDB.insertJsResult(extFolderName, js, md5, '', '', 'U', 0, 0, 0, 0)
										# Kary: Commented for Re-scan

								elif f.endswith('.html'):
									htmlPath = os.path.join(root, f)
									if os.stat(htmlPath).st_size != 0:
										html = htmlPath.split(verFolder + '/')[-1]
										allHtmls.append([html, 0, 0, 0, 0]) # ec, cs, dev, processed

						jsCount = 1
						# Kary: Commented for Re-scan
						jsCount = len(selectDB.selectJsResultByExtName(extFolderName))
						duplicateJsCount = len(selectDB.selectDupJsResultByExtName(extFolderName))
						# Kary: Commented for Re-scan
						
						if jsCount == 0:
							pass

						# Kary: Commented for Re-scan
						elif duplicateJsCount / jsCount >= 0.5:
							updateDB.updateJsResultDuplicate(extFolderName)
							commonCode.printDupExt()
						# Kary: Commented for Re-scan
						
						else:
							# manifest.json
							# Get Js & Html Files
							for root, dirs, files in os.walk(extFolder, topdown = False):
								for f in files:
									if f == 'manifest.json':
										manifestPath = os.path.join(root, f)
										allJSs, allHtmls = extManifest.readManifest(manifestPath, allJSs, allHtmls)
										break

							# Create ext folder in _Update
							newExtFolder = newNumFolder + '/' + extFolderName
							newVerFolder = newExtFolder + '/' + verNo
							commonCode.removeFolder(newExtFolder)
							commonCode.createFolder(newExtFolder)
							commonCode.createFolder(newVerFolder)

							# 2 Inline Scripts
							ecInlineScript, devInlineScript = '', ''

							# Get Js from Html
							allJSs, allHtmls, ecInlineScript, devInlineScript = extHtml.getAllJSs(allJSs, allHtmls, ecInlineScript, devInlineScript, verFolder)

							# allJSs have been extracted from 1) manifest file & 2) html file
							# Now extract from Js Files & beautifierJs
							assignTable, callTable = [], []
							allJSs, allHtmls, ecInlineScript, devInlineScript, assignTable, callTable = extJs.getAllJSs(extFolderName, allJSs, allHtmls, ecInlineScript, devInlineScript, verFolder, newVerFolder, assignTable, callTable)
							

							for j in allJSs:
								esprimaResult = ''
								if j[5] == 0: # error
									esprimaResult = 'N'
								else:
									esprimaResult = 'Y'
								updateDB.updateJsResultComponents(extFolderName, j[0], j[1], j[2], j[3], esprimaResult)
							# Kary: Commented for Re-scan
							for h in allHtmls:
								insertDB.insertHtmlResult(extFolderName, h[0], h[1], h[2], h[3])
							# Kary: Commented for Re-scan

							runtimeInAssignTable = False
							methodInAssignTable = False

							for c in assignTable:
								if 'connect' in c[1] or 'sendMessage' in c[1]:
									methodInAssignTable = True

								if 'runtime' in c[1]:
									runtimeInAssignTable = True

								if runtimeInAssignTable and methodInAssignTable:
									break

							if len(callTable) == 0:
								if runtimeInAssignTable and methodInAssignTable:
									insertDB.insertJsContent(extFolderName, assignTable, 'A')
							else:
								insertDB.insertJsContent(extFolderName, callTable, 'C')
								if len(assignTable) > 0:
									insertDB.insertJsContent(extFolderName, assignTable, 'A')

							ecInlineIndicator = 0
							devInlineIndicator = 0
							staticCheck = 'U'
							manualCheck = 'U'

							if ecInlineScript != '':
								extJs.writeInlineScriptToFile(ecInlineScript, newVerFolder, 'ec')
								ecInlineIndicator = 1
							if devInlineScript != '':
								extJs.writeInlineScriptToFile(devInlineScript, newVerFolder, 'dev')
								devInlineIndicator = 1


							if len(selectDB.selectNotEsprimaJsResult(extFolderName)):
								staticCheck = 'E'
								manualCheck = 'E'
								commonCode.printEsprimaError()

							elif ecInlineScript != '' or devInlineScript != '' or (runtimeInAssignTable and methodInAssignTable) or len(callTable) > 0:
								staticCheck = 'U'
								manualCheck = 'U'
								commonCode.printManualCheck()
							else:
								staticCheck = 'N'
								manualCheck = 'N'
								commonCode.removeFolder(newExtFolder)
								commonCode.printNoCrossExtMsg()

							insertDB.insertExtResult(extFolderName, ecInlineIndicator, devInlineIndicator, staticCheck, manualCheck, '')
							
							# commonCode.writeTable(allJSs)
							# commonCode.writeTable(allHtmls)

# ----- main -----


main()
