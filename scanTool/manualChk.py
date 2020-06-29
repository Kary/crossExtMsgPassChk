import sys, os
from getopt import getopt, GetoptError
import requests
from lxml import html
import mmap, contextlib
import re
from urllib.parse import urlparse


# Kary
import commonCode
import selectDB, updateDB
import extManifest
from config import parentFolder


# ----- printUsage -----
def printUsage():
	print('Usage:')
	print(commonCode.yellow('no arg'), 'Next 10 Extensions Pending for Manual Analysis')
	print(commonCode.yellow('-e'), 'Extension ID', commonCode.cyan('either -e or -n'))
	print(commonCode.yellow('-n'), 'Number of Extension', commonCode.cyan('either -e or -n'))
	print(commonCode.yellow('-r'), 'Update Result for Manual Analysis (Y or N)')
	print(commonCode.yellow('-c'), 'Update Comment for Manual Analysis')
	print(commonCode.green('Other Useful Scripts'))
	print(commonCode.yellow('search4Js.py'), 'extFolderName, keyword')
	print(commonCode.yellow('printJs.py'), 'jsFile, sLine, sCol, eLine, eCol')
# ----- printUsage -----


# ----- getArg -----
def getArg():
	extId, num, result, comment = '', '', '', ''
	argv = sys.argv[1:]
	opts, extraInput = [], []

	try: 
		opts, extraInput = getopt(argv, 'e:n:r:c:', ['extId=', 'num=', 'result=', 'comment='])
	except GetoptError:
		printUsage()
		sys.exit()

	if extraInput:
		printUsage()
		sys.exit()
	else:
		for opt, arg in opts:
			if opt in ('-e', '--extId'):
				extId = arg
			elif opt in ('-n', '--num'):
				num = arg
			elif opt in ('-r', '--result'):
				result = arg
			elif opt in ('-c', '--comment'):
				comment = arg

	if (extId != '' and num != '') or (extId == '' and num == ''):
		printUsage()
		sys.exit()

	if ((result != '' and comment == '') or (result == '' and comment != '')):
		printUsage()
		sys.exit()

	if result != '':
		if result in ['y', 'n', 'Y', 'N']:
			if result == 'y':
				result = 'Y'
			elif result == 'n':
				result = 'N'
		else:
			printUsage()
			sys.exit()
	return extId, num, result, comment
# ----- getArg -----


# ----- extractReceiverIds -----
def extractReceiverIds(string, file, selfExtId):
	extIds = []
	for i in re.finditer(br'[a-z]{32}', string):
		extId =  i[0].decode('utf-8')

		if extId not in extIds and extId != selfExtId:
			extIds.append(extId)
	
	return extIds
# ----- extractReceiverIds -----


# ----- extractDomains -----
def extractDomains(string, jsFile):
	# scheme://username:password@host:port/path?query#fragment
	scheme = 'https?:\/\/'

	username = '[-a-zA-Z0-9\+\.]+'
	pwd = '[^\s]+'
	usernameAndPwd = username + ':' + pwd
	userinfo = '((' + username + '@)|(' + usernameAndPwd + '@))?'

	www = 'www\.'
	wordsWHyphenDot = '[a-zA-Z0-9-]+\.'
	wordsWHyphenWoDot = '[a-zA-Z0-9-]+'
	host = '((' + www + '(' + wordsWHyphenDot + ')+' + wordsWHyphenWoDot + ')|((' + wordsWHyphenDot + ')+' + wordsWHyphenWoDot + '))'

	port = '(:[0-9]{1,5})?'

	others = '(\/[-a-zA-Z0-9()@:%_\+.~#?&//=]+)?'
	pattern = str.encode(scheme + userinfo + host + port + others)
	
	domains = []
	urls = []

	for u in re.finditer(pattern, string):
		if u[0] != b'https://clients2.google.com/service/update2/crx': # URL for update extension
			url = urlparse(u[0].decode('utf-8'))
			if u[0] not in urls:
				urls.append(u[0].decode())

			domain = '{uri.scheme}://{uri.netloc}/'.format(uri = url)
			if domain not in domains:
				domains.append(domain)

	return domains, urls
# ----- extractDomains -----


# ----- printDetail -----
def printDetail(extId, num):
	extDownload, extResult, htmlResult, jsResult = [], [], [], []
	callTable, assignTable = [], []
	ver = ''

	if extId != '':
		extDownload = selectDB.selectExtDownloadByExtId(extId)
		extResult = selectDB.selectExtResultByExtId(extId)
		htmlResult = selectDB.selectHtmlResultByExtId(extId)
		jsResult = selectDB.selectJsResultByExtId(extId)
		callTable = selectDB.selectCallTableByExtId(extId)
		assignTable = selectDB.selectAssignTableByExtId(extId)

	elif num != '':
		extDownload = selectDB.selectExtDownloadByExtNum(num)
		extResult = selectDB.selectExtResultByExtNum(num)
		htmlResult = selectDB.selectHtmlResultByExtNum(num)
		jsResult = selectDB.selectJsResultByExtNum(num)
		callTable = selectDB.selectCallTableByExtNum(num)
		assignTable = selectDB.selectAssignTableByExtNum(num)

	# ----- Basic Info -----
	if len(extDownload) > 0:
		num = extDownload[0][0]
		extId = extDownload[0][4]
		ver = extDownload[0][3]
		url = extDownload[0][5]
		print('Basic Info')

		if url != '':
			extPage =requests.get(url)

			if extPage.status_code in (400, 404) :
				print(commonCode.red('Removed from Chrome Web Store'))
				print(commonCode.yellow('No.:'), num, commonCode.yellow('Id:'), extId, commonCode.yellow('Version No.:'), ver)

			else:
				extPageContentTree = html.fromstring(extPage.content)

				# if htmlTree != None:
				nameTags = extPageContentTree.xpath('/html/head/meta[6]')
				for t in nameTags:
					name = t.get('content')

				descTags = extPageContentTree.xpath('/html/head/meta[7]')
				for d in descTags:
					desc = d.get('content')

				print(commonCode.yellow('No.:'), num, commonCode.yellow('Id:'), extId, commonCode.yellow('Version No.:'), ver)
				print(commonCode.yellow('Extension Name:'), name)
				print(commonCode.yellow('Description:'), desc)
			print(commonCode.yellow('URL:'), url)

		else:
			print(commonCode.yellow('No.:'), num, commonCode.yellow('Id:'), extId, commonCode.yellow('Version No.:'), ver)
		
		print(commonCode.yellow('Version Folder:'), str(num).zfill(6) + '_' + extId + '/' + ver)


	if len(extResult) > 0:
		if extResult[0][5] == 'U':
			print(commonCode.yellow('Status:'), 'Pending for Manual Check.')
		elif extResult[0][5] == 'N':
			print(commonCode.yellow('Status:'), 'No Collusion Attack.', extResult[0][6])
		elif extResult[0][5] == 'Y':
			print(commonCode.yellow('Status:'), 'Collusion Attack Found.', extResult[0][6])
		elif extResult[0][5] == 'E':
			print(commonCode.yellow('Status:'), 'Esprima Error.')

		elif extResult[0][5] == 'D':
			print(commonCode.yellow('Status:'), 'Similar Extension')

	# ----- Inline Scripts -----
		if extResult[0][2] == 1 or extResult[0][3] == 1:
			print('')
			if extResult[0][2] == 1:
				print(commonCode.yellow('Inline Script for Ext Core Found'))

			if extResult[0][3] == 1:
				print(commonCode.yellow('Inline Script for DevTool Found'))

	else:
		print(commonCode.yellow('Status:'), 'No Js File')

	# ----- Html -----
	if len(htmlResult) > 0:
		print('')
		ecHtml, devHtml = [], []
		for h in htmlResult:
			if h[3] == 1:
				ecHtml.append(h[2])
			elif h[5] == 1:
				devHtml.append(h[2])

		if len(ecHtml) > 0:
			commonCode.printResult('Html for Ext Core:', ecHtml)

		if len(devHtml) > 0:
			commonCode.printResult('Html for DevTool:', devHtml)

	# ----- Js -----
	if len(jsResult) > 0:
		print('')
		ecJs, ecDupJs, csJs, csDupJs, devJs, devDupJs = [], [], [], [], [], []
		for j in jsResult:
			if j[4] == '' and j[8] == 1:
				ecJs.append(j[2])
			elif j[4] == '' and j[9] == 1:
				csJs.append(j[2])
			elif j[4] == '' and j[10] == 1:
				devJs.append(j[2])
			elif j[4] != '' and j[8] == 1:
				ecDupJs.append([j[4], j[2]])
			elif j[4] != '' and j[9] == 1:
				csDupJs.append([j[4], j[2]])
			elif j[4] != '' and j[10] == 1:
				devDupJs.append([j[4], j[2]])

		if len(ecJs) > 0:
			commonCode.printResult('Js for Ext Core:', ecJs)

		if len(ecDupJs) > 0:
			sExtId = []
			print(commonCode.yellow('Dup Js for Ext Core:'))
			for j1 in ecDupJs:
				if j1[0] not in sExtId:
					sExtId.append(j1[0])
					ExtIds = []
					for j2 in ecDupJs:
						if j1[0] == j2[0]:
							ExtIds.append(j2[1])
					commonCode.printDupResult(j1[0], ExtIds)
					


		if len(csJs) > 0:
			commonCode.printResult('Js for Content Scripts:', csJs)

		if len(csDupJs) > 0:
			sExtId = []
			print(commonCode.yellow('Dup Js for Content Scripts'))
			for j1 in csDupJs:
				if j1[0] not in sExtId:
					sExtId.append(j1[0])
					ExtIds = []
					for j2 in csDupJs:
						if j1[0] == j2[0]:
							ExtIds.append(j2[1])
					commonCode.printDupResult(j1[0], ExtIds)

		if len(devJs) > 0:
			commonCode.printResult('Js for DevTool:', devJs)

		if len(devDupJs) > 0:
			sExtId = []
			print(commonCode.yellow('Dup Js for DevTool'))
			for j1 in devDupJs:
				if j1[0] not in sExtId:
					sExtId.append(j1[0])
					ExtIds = []
					for j2 in devDupJs:
						if j1[0] == j2[0]:
							ExtIds.append(j2[1])
					commonCode.printDupResult(j1[0], ExtIds)

	# ----- Call Table -----
	if len(callTable) > 0:
		print('')
		print(commonCode.yellow('Call Table'))
		for c in callTable:
			print(c[2], commonCode.green(c[4]), c[5], commonCode.cyan(c[6]), commonCode.cyan(c[7]), commonCode.cyan(c[8]), commonCode.cyan(c[9]))
	
	# ----- Assignment Table -----
	if len(assignTable) > 0:
		print('')
		print(commonCode.yellow('Assignment Table'))
		for a in assignTable:
			print(a[2], commonCode.green(a[4]), a[5], commonCode.cyan(a[6]), commonCode.cyan(a[7]), commonCode.cyan(a[8]), commonCode.cyan(a[9]))

	# --------------------
	# parentFolder = '/mnt/hgfs/karyBuffalo/HKUDissertation/chromeExt/ext'
	if len(extResult) > 0:
		numFolder = commonCode.getNumFolder(int(num))
		extFolder, verFolder = '', ''

		if extResult[0][4] == 'U': # Static Check: U, N, E, D
			extFolder = parentFolder + '/' + numFolder + '/' + str(num).zfill(6) + '_' + extId

		elif extResult[0][4] == 'N':
			extFolder = parentFolder + '/' + numFolder + '_NoMsg' + '/' + str(num).zfill(6) + '_' + extId

		elif extResult[0][4] == 'E':
			extFolder = parentFolder + '/' + numFolder + '_Esprima' + '/' + str(num).zfill(6) + '_' + extId
			
		else: # 'D'
			extFolder = parentFolder + '/' + numFolder + '_Dup' + '/' + str(num).zfill(6) + '_' + extId

		verFolder = extFolder + '/' + ver
		receiverIdList, urlList, domainList = [], [], []
		
		for root, dirs, files in os.walk(verFolder, topdown = False):
			for f in files:
				t = os.path.join(root, f)

				if os.stat(t).st_size != 0:
					if f.endswith('.html') or f.endswith('.js') or f.endswith('.json') or f.endswith('.xml'):
						tb = open(t, 'rb', 0)
						
						with contextlib.closing(mmap.mmap(tb.fileno(), 0, access = mmap.ACCESS_READ)) as s:
							# get extension ids
							receiverIds = extractReceiverIds(s, f, extId)
							if len(receiverIds) > 0:
								receiverIdList.append([t.split(verFolder + '/')[-1], receiverIds])

							# get urls
							domains, urls = extractDomains(s, f)
							if len(urls) > 0:
								urlList.append([t.split(verFolder + '/')[-1], urls])
							if len(domains) > 0:
								domainList.append([t.split(verFolder + '/')[-1], domains])

						tb.close()

		# ----- Possible Receiver List -----
		if len(receiverIdList) > 0:
			print('')
			print(commonCode.yellow('Possible Receiver List'))
			for rl in receiverIdList:
				for receiverId in rl[1]:
					receiverDb = selectDB.selectExtDownloadByExtId(receiverId)
					if len(receiverDb) == 0:
						print(rl[0], commonCode.cyan(receiverId), 'Not Found in DB')
					else:
						if receiverDb[0][2] == 1: # Downloaded
							print(rl[0], commonCode.cyan(receiverId), commonCode.yellow('Found in DB'), receiverDb[0][0], '(', receiverDb[0][3], ')', receiverDb[0][5])
						else:
							print(rl[0], commonCode.cyan(receiverId), commonCode.yellow('Found in DB But Not Downloaded'), receiverDb[0][0], receiverDb[0][3])

		# ----- Additional Info in Manifest File -----
		print('')
		print(commonCode.yellow('Additional Info in Manifest File'))
		managementAPI = extManifest.addInfoManifest(verFolder + '/' + 'manifest.json')

		# ----- Js Files with Keyword: management
		if managementAPI:
			print(commonCode.yellow('Js Files with Keyword: management'))
			if not commonCode.Search4Keyword(extFolder, 'management'):
				print('Not Found')

		# ----- Domain List -----
		if len(domainList) > 0:
			print('')
			print(commonCode.yellow('Domain List'))
			for dl in domainList:
				print(commonCode.cyan(dl[0]), dl[1])

		# ----- Url List -----
		if len(urlList) > 0:
			print('')
			print(commonCode.yellow('Url List'))
			for ul in urlList:
				print(commonCode.cyan(ul[0]), ul[1]) 
# ----- printDetail -----


# ----- main -----
def main():
	if len(sys.argv) == 1: 
		print(commonCode.green('Random Extensions for Manual Analysis:'))
		extFolderNames = selectDB.randomExtForManualAnalysis(10)
		for e in extFolderNames:
			print(e)
		print(commonCode.green('Number of Extensions Pending for Manual Analysis:'), selectDB.numExtForManualAnalysis()[0][0])
		printUsage()

	else:
		extId, num, result, comment = getArg()
		if result != '': # Update on DB
			if extId != '':
				updateDB.updateExtResultByExtId(extId, result, comment)
			elif num != '':
				updateDB.updateExtResultByExtNum(num, result, comment)
			print('Updated on DB')

		else:
			printDetail(extId, num)
# ----- main -----


main()