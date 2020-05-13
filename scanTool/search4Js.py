import os, sys
import re

# Kary
import commonCode
from config import parentFolder


# ----- printUsage -----
def printUsage():
	print('python3 XXX.py extFolderName, keyword')
	sys.exit()
# ----- printUsage -----

# ----- main -----
def main():
	if len(sys.argv) != 3:
		printUsage()
	else:
		extFolderName = sys.argv[1]
		keyword = sys.argv[2]

		num = extFolderName.split('_')[0].lstrip('0')
		numFolder = commonCode.getNumFolder(int(num))
	
		if os.path.isdir(parentFolder + '/' + numFolder + '/' + extFolderName):
			commonCode.Search4Keyword(parentFolder + '/' + numFolder + '/' + extFolderName, keyword)


		elif os.path.isdir(parentFolder + '/' + numFolder + '_Dup' + '/' + extFolderName):
			print('In Dup Folder')
			commonCode.Search4Keyword(parentFolder + '/' + numFolder + '_Dup' + '/' + extFolderName, keyword)


		elif os.path.isdir(parentFolder + '/' + numFolder + '_Esprima' + '/' + extFolderName):
			print('In Esprima Folder')
			commonCode.Search4Keyword(parentFolder + '/' + numFolder + '_Esprima' + '/' + extFolderName, keyword)


		elif os.path.isdir(parentFolder + '/' + numFolder + '_NoMsg' + '/' + extFolderName):
			print('In NoMsg Folder')
			commonCode.Search4Keyword(parentFolder + '/' + numFolder + '_NoMsg' + '/' + extFolderName, keyword)

		elif os.path.isdir(parentFolder + '/' + numFolder + '_NoJs' + '/' + extFolderName):
			print('In NoJs Folder')
			commonCode.Search4Keyword(parentFolder + '/' + numFolder + '_NoJs' + '/' + extFolderName, keyword)

		else:
			print('Ext Folder Not Found')
# ----- main -----

main()