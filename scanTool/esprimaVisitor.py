import esprima
import re
# Kary
import commonCode
from reservedWords import reservedWords


# ----- class  -----
class esprimaVisitor(esprima.NodeVisitor):
	def __init__(self, extId, js, htmlKeywords, jsKeywords):
		self.assignTable = []
		self.callTable = []
		# self.funcTable = []
		self.literalTable = []

		self.extId = extId
		self.js = js
		self.htmlKeywords = htmlKeywords
		self.jsKeywords = jsKeywords

		self.defNoSymCall = {
			'ArrayExpression': self.ArrayExpressionNoSym,
			'ArrowFunctionExpression': self.getArrowFunctionExpressionNoSym,
			'BinaryExpression': self.getBinaryExpressionNoSym,
			'CallExpression': self.getCallExpressionNoSym,
			'FunctionExpression': self.getFunctionExpressionNoSym,
			'Identifier': self.getIdentifierNoSym,
			'Literal': self.getLiteralNoSym,
			'MemberExpression': self.getMemberExpressionNoSym,
			'NewExpression': self.getNewExpressionNoSym,
			'ObjectExpression': self.getObjectExpressionNoSym,
			'SpreadElement': self.getSpreadElementNoSym,
			'ThisExpression': self.getThisExpressionNoSym,
			'UnaryExpression': self.getUnaryExpressionNoSym
		}
		self.defCall = {
			'ArrayExpression': self.ArrayExpression,
			'ArrowFunctionExpression': self.getArrowFunctionExpression,
			'BinaryExpression': self.getBinaryExpression,
			'CallExpression': self.getCallExpression,
			'FunctionExpression': self.getFunctionExpression,
			'Identifier': self.getIdentifier,
			'Literal': self.getLiteral,
			'MemberExpression': self.getMemberExpression,
			'NewExpression': self.getNewExpression,
			'ObjectExpression': self.getObjectExpression,
			'SpreadElement': self.getSpreadElement,
			'ThisExpression': self.getThisExpression,
			'UnaryExpression': self.getUnaryExpression
		}


	# --------------------------------------------------
	def visit_CallExpression(self, node):
		# callee & arguments
		# Get firstParam
		if len(node.arguments) > 0: # sendMessage & connect
			methodKeywords = []
			validateCallee = False
			validateFirstParam = False

			# Get Keywords
			for c in self.defNoSymCall:
				if node.callee.type == c:
					methodKeywords = self.defNoSymCall[c](node.callee).split('+++++')

			if len(methodKeywords) > 0:
				if not any(m in methodKeywords for m in reservedWords):
					if methodKeywords[-1] in ['connect', 'sendMessage']:
						if methodKeywords[-1] == 'sendMessage':
							if len(node.arguments) > 1:
								if node.arguments[0].type != 'ObjectExpression' and node.arguments[0].type != 'ArrayExpression':
									validateCallee = True
						else: # connect
							if len(node.arguments) > 0:
								if node.arguments[0].type != 'ObjectExpression' and node.arguments[0].type != 'ArrayExpression':
									validateCallee = True

			callee, firstParam = '', ''

			if validateCallee:
				for c in self.defCall:				
					if node.callee.type == c:
						callee = self.defCall[c](node.callee)
					if node.arguments[0].type == c:
						firstParam = self.defCall[c](node.arguments[0])

				if firstParam.startswith('\'') and firstParam.endswith('\''):
					if firstParam != '\'' + self.extId + '\'' and firstParam != '\'nmmhkkegccagdldgiimedpiccmgmieda\'' and \
						firstParam != '\'ahfgeienlihckogmohjhadlkjgocpleb\'' and re.match('\'[a-z]{32}\'', str(firstParam)):
						validateFirstParam = True
				else:
					if firstParam != 'chrome.runtime.id' and firstParam != 'browser.runtime.id' and firstParam != 'undefined' and firstParam != 'null' and not firstParam.isdigit() and firstParam != 'True' and firstParam != 'False' and firstParam != 'void(0)' and not firstParam.startswith('JSON.stringify'):
						validateFirstParam = True

			if validateFirstParam:
				self.callTable.append([callee, firstParam, node.loc, self.js])

		self.generic_visit(node)


	def visit_AssignmentExpression(self, node): # a = b
		# operator, left & right
		if node.right:
			if node.operator == '=':
				methodKeywords = []

				# Get Keywords
				for c in self.defNoSymCall:
					if node.right.type == c:
						methodKeywords = self.defNoSymCall[c](node.right).split('+++++')

				# Append to assignTable
				if node.right.type in ['ArrayExpression', 'ObjectExpression']:
					for m in methodKeywords:
						if m in ['browser', 'chrome', 'runtime', 'connect', 'sendMessage']: # 'window'
							left, right = '', ''
							for c in self.defCall:
								if node.left.type == c:
									left = self.defCall[c](node.left)
								if node.right.type == c:
									right = self.defCall[c](node.right)
							self.assignTable.append([left, right, node.loc, self.js])
							break
				else:
					if len(methodKeywords) > 0:
						if methodKeywords[-1] in ['browser', 'chrome', 'runtime', 'connect', 'sendMessage']: # 'window'
							left, right = '', ''
							for c in self.defCall:
								if node.left.type == c:
									left = self.defCall[c](node.left)
								if node.right.type == c:
									right = self.defCall[c](node.right)
							self.assignTable.append([left, right, node.loc, self.js])

		self.generic_visit(node)


	def visit_VariableDeclarator(self, node): # var a = b
		# id & init
		if node.init:
			methodKeywords = []

			# Get Keywords
			for c in self.defNoSymCall:
				if node.init.type == c:
					methodKeywords = self.defNoSymCall[c](node.init).split('+++++')

			# Append to assignTable
			if node.init.type in ['ArrayExpression', 'ObjectExpression']:
				for m in methodKeywords:
					if m in ['browser', 'chrome', 'runtime', 'connect', 'sendMessage']: # 'window'
						left, right = '', ''
						for c in self.defCall:
							if node.id.type == c:
								left = self.defCall[c](node.id)
							if node.init.type == c:
								right = self.defCall[c](node.init)
						self.assignTable.append([left, right, node.loc, self.js])
						break
			else:
				if len(methodKeywords) > 0:
					if methodKeywords[-1] in ['browser', 'chrome', 'runtime', 'connect', 'sendMessage']: # 'window'
						left, right = '', ''
						for c in self.defCall:
							if node.id.type == c:
								left = self.defCall[c](node.id)
							if node.init.type == c:
								right = self.defCall[c](node.init)
						self.assignTable.append([left, right, node.loc, self.js])

		self.generic_visit(node)


	def visit_Literal(self, node):
		if node.value: # string, regexp, boolean, number
			if type(node.value) == str:
				if not (node.value.startswith('re.compile') or node.value.startswith('http://') or node.value.startswith('https://') or node.value.startswith(' ')) and node.value.strip() != '' and len(node.value) < 180: # 256 - C:\Users\<Your_User_Name>\AppData\Local\Google\Chrome\User Data\Default\Extensions
					# \ < > : " | ? *
					if not ('\\' in str(node.value) or '>' in str(node.value) or '<' in str(node.value) or ':' in str(node.value) or '"' in str(node.value) or '|' in str(node.value) or '?' in str(node.value) or '*' in str(node.value) or '\x00' in str(node.value)):

						if node.value not in self.literalTable:
							appendToLiteral = False
							for j in self.jsKeywords:
								if j in node.value:
									appendToLiteral = True
									break

							for h in self.htmlKeywords:
								if appendToLiteral:
									break
								elif h in node.value:
									appendToLiteral = True
									break
							
							if appendToLiteral:
								try:
									node.value.encode('utf-8')
									self.literalTable.append(node.value)
								except UnicodeEncodeError as e:
									pass
								
		self.generic_visit(node)
	# --------------------------------------------------


	# --------------------------------------------------
	def returnAssignTable(self):
		return self.assignTable


	def returnCallTable(self):
		return self.callTable


	# def returnFuncTable(self):
	# 	return self.funcTable

	def returnLiteralTable(self):
		return self.literalTable
	# --------------------------------------------------

	# --------------------------------------------------

	def getArgElementParam(self, node):
		for c in self.defCall:
			if node.type == c:
				return self.defCall[c](node)

		return ''

	def ArrayExpression(self, node):
		# elements
		pStr = ''
		if node.elements:
			for i in range(0, len(node.elements)):
				if node.elements[i]:
					if i == 0:
						pStr = self.getArgElementParam(node.elements[i])
					else:
						pStr = pStr + ',' + self.getArgElementParam(node.elements[i])
				else:
					if i != 0:
						pStr = pStr + ','
		return '[' + pStr + ']'


	def getArrowFunctionExpression(self, node):
		# params & body
		pStr = ''
		if node.params:
			for i in range(0, len(node.params)):
				if i == 0:
					pStr = self.getArgElementParam(node.params[i])
				else:
					pStr = pStr + ',' + self.getArgElementParam(node.params[i])

		for c in self.defCall:
			if node.body.type == c:
				return '(' + pStr + ')=>' + self.defCall[c](node.body)

		return ''


	def getBinaryExpression(self, node):
		# operator, left & right
		if node.operator == '+':
			for l in self.defCall:
				for r in self.defCall:
					if node.left.type == l and node.right.type == r:
						return self.defCall[l](node.left) + '+' + self.defCall[r](node.right)

		return ''


	def getCallExpression(self, node):
		# callee & arguments
		pStr = ''
		if node.arguments:
			for i in range(0, len(node.arguments)):
				if i == 0:
					pStr = self.getArgElementParam(node.arguments[i])
				else:
					pStr = pStr + ',' + self.getArgElementParam(node.arguments[i])
		
		for c in self.defCall:
			if node.callee.type == c:
				return self.defCall[c](node.callee) + '(' + pStr + ')'

		return ''


	def getFunctionExpression(self, node):
		# id, params, body & arguments
		Id, params, body, args = '', '', '', ''

		if node.id:
			for c in self.defCall:
				if node.id.type == c:
					Id = self.defCall[c](node.id)

		if node.params:
			for i in range(0, len(node.params)):
				if i == 0:
					params = self.getArgElementParam(node.params[i])
				else:
					params = params + ',' + self.getArgElementParam(node.params[i])

		if node.body:
			for c in self.defCall:
				if node.body.type == c:
					body = self.defCall[c](node.body)
		
		if node.arguments:
			for i in range(0, len(node.arguments)):
				if i == 0:
					args = self.getArgElementParam(node.arguments[i])
				else:
					args = args + ',' + self.getArgElementParam(node.arguments[i])

		funcExpr = ''

		if Id != '':
			funcExpr = 'function' + ' ' + Id + '(' + params + ')' + '{' + body + '}'
		else:
			funcExpr = 'function' + '(' + params + ')' + '{' + body + '}'

		if args != '':
			funcExpr = funcExpr + '(' + args + ')'

		return funcExpr


	def getIdentifier(self, node):
		return node.name


	def getLiteral(self, node):
		if type(node.value) == int or node.value == True or node.value == False: # boolean, number
			return str(node.value)

		elif node.value: # string, regexp
			return '\'' + str(node.value) + '\'' 

		else: # null
			return 'null'


	def getMemberExpression(self, node):
		# object & property
		for o in self.defCall:
			for p in self.defCall:
				if node.object.type == o and node.property.type == p:
					if node.computed:
						return self.defCall[o](node.object) + '[' + self.defCall[p](node.property) + ']'
					else:
						return self.defCall[o](node.object) + '.' + self.defCall[p](node.property)

		return ''


	def getNewExpression(self, node):
		# callee & args
		pStr = ''
		if node.arguments:
			for i in range(0, len(node.arguments)):
				if i == 0:
					pStr = self.getArgElementParam(node.arguments[i])
				else:
					pStr = pStr + ',' + self.getArgElementParam(node.arguments[i])
		
		for c in self.defCall:
			if node.callee.type == c:
				return 'new ' + self.defCall[c](node.callee) + '(' + pStr + ')'

		return ''


	def getObjectExpression(self, node):
		# properties
		# key & value
		# {key: value}
		pStr = ''
		if node.properties:
			for i in range(0, len(node.properties)):
				if i == 0:
					pStr = self.getObjectExpressionProp(node.properties[i])
				else:
					pStr = pStr + ',' + self.getObjectExpressionProp(node.properties[i])
			
		return '{' + pStr + '}'


	def getObjectExpressionProp(self, node):
		if node.type == 'Property':
			for k in self.defCall:
				for v in self.defCall:
					if node.key.type == k and node.value.type == v:
						return self.defCall[k](node.key) + ':' + self.defCall[v](node.value)

		return ''


	def getSpreadElement(self, node):
		# argument
		for c in self.defCall:
			if node.argument.type == c:
				return '...' + self.defCall[c](node.argument)

		return ''


	def getThisExpression(self, node):
		return 'this'


	def getUnaryExpression(self, node):
		# prefix, operator, argument
		if node.prefix == True and node.operator == 'void':
			for c in self.defCall:
				if node.argument.type == c:
					return 'void' + '(' + self.defCall[c](node.argument) + ')' 

		return ''
	# --------------------------------------------------


	# --------------------------------------------------
	def getArgElementParamNoSym(self, node):
		for c in self.defNoSymCall:
			if node.type == c:
				return self.defNoSymCall[c](node)

		return ''

	def ArrayExpressionNoSym(self, node):
		# elements
		pStr = ''
		if node.elements:
			for i in range(0, len(node.elements)):
				if node.elements[i]:
					if i == 0:
						pStr = self.getArgElementParamNoSym(node.elements[i])
					else:
						pStr = pStr + '+++++' + self.getArgElementParamNoSym(node.elements[i])
		return pStr


	def getArrowFunctionExpressionNoSym(self, node):
		# params & body
		pStr = ''
		if node.params:
			for i in range(0, len(node.params)):
				if i == 0:
					pStr = self.getArgElementParamNoSym(node.params[i])
				else:
					pStr = pStr + '+++++' + self.getArgElementParamNoSym(node.params[i])

		for c in self.defNoSymCall:
			if node.body.type == c:
				return pStr + '+++++' + self.defNoSymCall[c](node.body)

		return ''


	def getBinaryExpressionNoSym(self, node):
		# operator, left & right
		if node.operator == '+':
			for l in self.defNoSymCall:
				for r in self.defNoSymCall:
					if node.left.type == l and node.right.type == r:
						return self.defNoSymCall[l](node.left) + '+++++' + self.defNoSymCall[r](node.right)

		return ''


	def getCallExpressionNoSym(self, node):
		# callee & arguments
		pStr = ''
		if node.arguments:
			for i in range(0, len(node.arguments)):
				if i == 0:
					pStr = self.getArgElementParamNoSym(node.arguments[i])
				else:
					pStr = pStr + '+++++' + self.getArgElementParamNoSym(node.arguments[i])
		
		for c in self.defNoSymCall:
			if node.callee.type == c:
				return self.defNoSymCall[c](node.callee) + '+++++' + pStr

		return ''


	def getFunctionExpressionNoSym(self, node):
		# id, params, body & arguments
		Id, params, body, args = '', '', '', ''

		if node.id:
			for c in self.defNoSymCall:
				if node.id.type == c:
					Id = self.defNoSymCall[c](node.id)

		if node.params:
			for i in range(0, len(node.params)):
				if i == 0:
					params = self.getArgElementParamNoSym(node.params[i])
				else:
					params = params + '+++++' + self.getArgElementParamNoSym(node.params[i])

		if node.body:
			for c in self.defNoSymCall:
				if node.body.type == c:
					body = self.defNoSymCall[c](node.body)

		if node.arguments:
			for i in range(0, len(node.arguments)):
				if i == 0:
					args = self.getArgElementParamNoSym(node.arguments[i])
				else:
					args = args + '+++++' + self.getArgElementParamNoSym(node.arguments[i])

		funcExpr = ''

		if Id != '':
			funcExpr = Id + '+++++' + params + '+++++' + body
		else:
			funcExpr = params + '+++++' + body

		if args != '':
			funcExpr = funcExpr + '+++++' + args

		return funcExpr


	def getIdentifierNoSym(self, node):
		return self.getIdentifier(node)


	def getLiteralNoSym(self, node):
		if node.value: # boolean, number, string, regexp
			return str(node.value)

		else: # null
			return ''


	def getMemberExpressionNoSym(self, node):
		# object & property
		for o in self.defNoSymCall:
			for p in self.defNoSymCall:
				if node.object.type == o and node.property.type == p:
					#if node.computed:
					return self.defNoSymCall[o](node.object) + '+++++' + self.defNoSymCall[p](node.property)
					# else:

		return ''


	def getNewExpressionNoSym(self, node):
		# callee & arguments
		pStr = ''
		if node.arguments:
			for i in range(0, len(node.arguments)):
				if i == 0:
					pStr = self.getArgElementParamNoSym(node.arguments[i])
				else:
					pStr = pStr + '+++++' + self.getArgElementParamNoSym(node.arguments[i])
		
		for c in self.defNoSymCall:
			if node.callee.type == c:
				return self.defNoSymCall[c](node.callee) + '+++++' + pStr

		return ''


	def getObjectExpressionNoSym(self, node):
		# properties
		# key & value
		# {key: value}
		pStr = ''
		if node.properties:
			for i in range(0, len(node.properties)):
				if i == 0:
					pStr = self.getObjectExpressionPropNoSym(node.properties[i])
				else:
					pStr = pStr + '+++++' + self.getObjectExpressionPropNoSym(node.properties[i])
			
		return pStr


	def getObjectExpressionPropNoSym(self, node):
		if node.type == 'Property':
			for k in self.defNoSymCall:
				for v in self.defNoSymCall:
					if node.key.type == k and node.value.type == v:
						return self.defNoSymCall[k](node.key) + '+++++' + self.defNoSymCall[v](node.value)

		return ''


	def getSpreadElementNoSym(self, node):
		# argument
		for c in self.defNoSymCall:
			if node.argument.type == c:
				return self.defNoSymCall[c](node.argument)

		return ''


	def getThisExpressionNoSym(self, node):
		return ''


	def getUnaryExpressionNoSym(self, node):
		# prefix, operator, argument
		if node.prefix == True and node.operator == 'void':
			for c in self.defNoSymCall:
				if node.argument.type == c:
					return self.defNoSymCall[c](node.argument)

		return ''
	# --------------------------------------------------