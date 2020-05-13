import sys


def getTargetPart(jsFile, sLine, sCol, eLine, eCol):

	js = open(jsFile, 'r')
	jsLines = js.readlines()
	js.close()
	
	# sPart = []
	tPart = []
	# fPart = []

	if sLine > eLine:
		print('invalid position')
		sys.exit()

	elif sLine == eLine:
		if sCol > eCol:
			print('invalid position')
			sys.exit()

		elif sCol == eCol:
			pass
			
		elif sCol < eCol:
			for i in range (0, len(jsLines)):
				if i < sLine - 1:
					# sPart.append(jsLines[i])
					pass

				elif i == sLine - 1:
					# sChars = ''
					tChars = ''
					# fChars = ''
					for j in range (0, len(jsLines[i])):
						if j < sCol:
							# sChars = sChars + jsLines[i][j]
							pass

						elif sCol <= j < eCol:
							tChars = tChars + jsLines[i][j]

						elif j >= eCol:
							# fChars = fChars + jsLines[i][j]
							pass
					# sPart.append(sChars)
					tPart.append(tChars)
					# fPart.append(fChars)

				elif i > sLine - 1:
					# fPart.append(jsLines[i])
					pass

	elif sLine < eLine:
		for i in range (0, len(jsLines)):
			if i < sLine - 1:
				# sPart.append(jsLines[i])
				pass

			elif i == sLine - 1:
				# sChars = ''
				tChars = ''
				for j in range (0, len(jsLines[i])):
					if j < sCol:
						# sChars = sChars + jsLines[i][j]
						pass

					else:
						tChars = tChars + jsLines[i][j]

				# sPart.append(sChars)
				tPart.append(tChars)

			elif i < eLine - 1:
				tPart.append(jsLines[i])

			elif i == eLine - 1:
				tChars = ''
				# fChars = ''
				for j in range (0, len(jsLines[i])):
					if j < eCol:
						tChars = tChars + jsLines[i][j]

					else:
						# fChars = fChars + jsLines[i][j]
						pass
				tPart.append(tChars)
				# fPart.append(fChars)

			elif i > eLine - 1:
				# fPart.append(jsLines[i])
				pass
	
	# return sPart, tPart, fPart
	return tPart
# ----- printFile -----


# ----- printUsage -----
def printUsage():
	print('python3 XXX.py jsFile, sLine, sCol, eLine, eCol')
	print('/mnt/hgfs/karyBuffalo/HKUDissertation/chromeExt/ext/010000_Update/')
	sys.exit()
# ----- printUsage -----


# ----- main -----
def main():
	if len(sys.argv) != 6:
		printUsage()
	else:
		tPart = getTargetPart(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))
		for t in tPart:
			print(t)
# ----- main -----

main()