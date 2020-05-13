from lxml import etree
import os

# Kary
import commonCode


# ----- getAllJSs -----
def getAllJSs(allJSs, allHtmls, ecInlineScript, devInlineScript, verFolder):
	for i in range(0, len(allHtmls)): # html, ec, cs, dev, processed
		if allHtmls[i][1] + allHtmls[i][2] + allHtmls[i][3] > 0 and allHtmls[i][4] == 0:
			html = allHtmls[i][0]
			htmlPath = verFolder + '/' + html
			if os.path.exists(htmlPath):
				allHtmls[i][4] = 1
				allJSs, ecInlineScript, devInlineScript = getJSsForEachHtml(html, verFolder, allJSs, allHtmls, ecInlineScript, devInlineScript)
	return allJSs, allHtmls, ecInlineScript, devInlineScript
# ----- getAllJSs -----


# ----- getJSsForEachHtml -----
def getJSsForEachHtml(html, verFolder, allJSs, allHtmls, ecInlineScript, devInlineScript):
	scriptTypes = commonCode.getFilesScriptTypeFromTable(allHtmls, html)

	htmlPath = verFolder + '/' + html
	# pageFileName = os.path.basename(htmlPath)
	htmlFolder = os.path.dirname(htmlPath)

	if os.stat(htmlPath).st_size != 0:
		htmlFile = open(htmlPath, 'r', encoding = 'ISO-8859-1')
		htmlParser = etree.HTMLParser()
		htmlData = etree.parse(htmlFile, htmlParser)
		htmlFile.close()

		htmlTree = htmlData.getroot()

		if htmlTree != None:
			scriptTags = htmlData.findall('.//script')
			for t in scriptTags:
				src = t.get('src')
				if src != None:
					if src.endswith('.js'):
						js = src
						if js.startswith('../'):
							jsPath = os.path.normpath(htmlFolder + '/' + js).split(verFolder + '/')[-1]

						elif js.startswith('/'):
							jsPath = js.lstrip('/')

						else:
							jsPath = os.path.normpath(htmlFolder + '/' + js).split(verFolder + '/')[-1]
					
						for s in scriptTypes:
							commonCode.updateTable(allJSs, jsPath, s)

				dataMain = t.get('data-main')
				if dataMain != None:					
					if not dataMain.endswith('.js'):
						js = dataMain + '.js'
					else:
						js = dataMain

					for s in scriptTypes:
						commonCode.updateTable(allJSs, js, s)

				inlineScriptType = t.get('type')
				if inlineScriptType == None:
					inlineScript = t.text
					if inlineScript != None:
						if inlineScript.strip() != '':
							for s in scriptTypes:
								if s == 'ec':
									ecInlineScript = ecInlineScript + inlineScript
								elif s == 'dev':
									devInlineScript = devInlineScript + inlineScript

				elif 'javascript' in inlineScriptType:
					inlineScript = t.text
					if inlineScript != None:
						if inlineScript.strip() != '':
							for s in scriptTypes:
								if s == 'ec':
									ecInlineScript = ecInlineScript + inlineScript
								elif s == 'dev':
									devInlineScript = devInlineScript + inlineScript

	return allJSs, ecInlineScript, devInlineScript
# ----- getJSsForEachHtml -----