import json
import os

# Kary
import commonCode


# ----- readManifest -----
def readManifest(manifestPath, allJSs, allHtmls):
	manifestJson = open(manifestPath, 'r')
	manifestJsonData = json.loads(manifestJson.read().encode().decode('utf-8-sig'), strict = False)

	# ----- Get All JS -----
	# background: html or js
	# + inline JS
	if 'background' in manifestJsonData:
		if 'page' in manifestJsonData['background']:
			try:
				if type(manifestJsonData['background']['page']) == list:
					html = os.path.normpath(manifestJsonData['background']['page'][0].lstrip('./'))
				else:
					html = os.path.normpath(manifestJsonData['background']['page'].lstrip('./'))
				allHtmls = commonCode.updateTable(allHtmls, html, 'ec')
			except TypeError as e:
				pass
				
		elif 'scripts' in manifestJsonData['background']:
			for i in range(0, len(manifestJsonData['background']['scripts'])):
				js = os.path.normpath(manifestJsonData['background']['scripts'][i].lstrip('./'))
				allJSs = commonCode.updateTable(allJSs, js, 'ec')

	# content_scripts: js
	# + programmatically injected cs
	if 'content_scripts' in manifestJsonData:
		for i in range(0, len(manifestJsonData['content_scripts'])):
			if 'js' in manifestJsonData['content_scripts'][i]:
				for j in range(0, len(manifestJsonData['content_scripts'][i]['js'])):
					js = os.path.normpath(manifestJsonData['content_scripts'][i]['js'][j].lstrip('./'))
					allJSs = commonCode.updateTable(allJSs, js, 'cs')

	# options_page
	if 'options_page' in manifestJsonData:
		if type(manifestJsonData['options_page']) == list:
			html = os.path.normpath(manifestJsonData['options_page'][0].lstrip('./'))
		else:
			html = os.path.normpath(manifestJsonData['options_page'].lstrip('./'))
		allHtmls = commonCode.updateTable(allHtmls, html, 'ec')

	# options_ui
	if 'options_ui' in manifestJsonData:
		if 'page' in manifestJsonData['options_ui']:
			if type(manifestJsonData['options_ui']['page']) == list:
				html = os.path.normpath(manifestJsonData['options_ui']['page'][0].lstrip('./'))
			else:
				html = os.path.normpath(manifestJsonData['options_ui']['page'].lstrip('./'))
			allHtmls = commonCode.updateTable(allHtmls, html, 'ec')

	# browser_action: html
	# + chrome.browserAction.setPopup {popup: 'popup.html'} 
	# + chrome windows.create {url: chrome.runtime.getURL("popup.html"), type: "popup"}
	if 'browser_action' in manifestJsonData:
		if 'default_popup' in manifestJsonData['browser_action']:
			if type(manifestJsonData['browser_action']['default_popup']) == list:
				html = os.path.normpath(manifestJsonData['browser_action']['default_popup'][0].lstrip('./'))
			else:
				html = os.path.normpath(manifestJsonData['browser_action']['default_popup'].lstrip('./'))
			allHtmls = commonCode.updateTable(allHtmls, html, 'ec')
	
	# page_action: html
	# + chrome.pageAction.setPopup
	# + chrome windows.create
	elif 'page_action' in manifestJsonData:
		if 'default_popup' in manifestJsonData['page_action']:
			if type(manifestJsonData['page_action']['default_popup']) == list:
				html = os.path.normpath(manifestJsonData['page_action']['default_popup'][0].lstrip('./'))
			else:
				html = os.path.normpath(manifestJsonData['page_action']['default_popup'].lstrip('./'))
			allHtmls = commonCode.updateTable(allHtmls, html, 'ec')

	# devtools_page: html
	# + chrome.devtools.panels.create: panel
	# + chrome.devtools.panels.elements.createSidebarPane: sidebar pane
	# + + setPage, setObject, setExpression
	if 'devtools_page' in manifestJsonData:
		if type(manifestJsonData['devtools_page']) == list:
			html = os.path.normpath(manifestJsonData['devtools_page'][0].lstrip('./'))
		else:
			html = os.path.normpath(manifestJsonData['devtools_page'].lstrip('./'))
		allHtmls = commonCode.updateTable(allHtmls, html, 'dev')

	manifestJson.close()

	return allJSs, allHtmls
# ----- readManifest -----

	
# ----- addInfoManifest -----
def addInfoManifest(manifestPath):
	manifestJson = open(manifestPath, 'r')
	manifestJsonData = json.loads(manifestJson.read().encode().decode('utf-8-sig'), strict = False)

	managementAPI = False
	# permissions field
	permissions = ''
	if 'permissions' in manifestJsonData:
		for i in range(0, len(manifestJsonData['permissions'])):
			permissions = permissions + manifestJsonData['permissions'][i] + ' '
			if manifestJsonData['permissions'][i] == 'management':
				managementAPI = True
		print(commonCode.cyan('Permissions:'), permissions)

	optPermissions = ''
	# optional_permissions field
	if 'optional_permissions' in manifestJsonData:
		for i in range(0, len(manifestJsonData['optional_permissions'])):
			optPermissions = optPermissions + manifestJsonData['optional_permissions'][i] + ' '
		print(commonCode.cyan('Optional Permission'), optPermissions)

	senders = ''
	# externally_connectable manifest key with ids property
	if 'externally_connectable' in manifestJsonData:
		if 'ids' in manifestJsonData['externally_connectable']:
			for i in range(0, len(manifestJsonData['externally_connectable']['ids'])):
				senders = senders + manifestJsonData['externally_connectable']['ids'][i] + ' '
			print(commonCode.cyan('Allow Msg from Other Extensions:'), senders)
	else:
		print(commonCode.cyan('Allow Msg from Other Extensions'))

	# web_accessible_resources
	if 'web_accessible_resources' in manifestJsonData:
		print(commonCode.cyan('Contain Web Accessible Resources'))

	manifestJson.close()

	return managementAPI
# ----- addInfoManifest -----