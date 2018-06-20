import re
import ply.lex as lex
from ply.lex import TOKEN

with open("hello_world_comment_removal.cpp", "r") as f:
	x = f.readlines()

o = open("hello_world_final_processed.cpp", "w")

macros = {}

tokens = ("IDENTIFIER",)


# new_line = chr(10)
# multi_LINE_COMMENTS = r'/\*(.|' + new_line + r')*?\*/'
# multi_LINE_COMMENTS = r'/\*([^/]|\/[^*])*\*/'

def t_IDENTIFIER(t):
	# This checks if the lexeme is an identifier or a keyword and returns accordingly
    r'[a-zA-Z_][a-zA-Z0-9_\-]*'
    if(t.value in list(macros.keys())):
    	return t

'''
@TOKEN(multi_LINE_COMMENTS)
def t_MULTI_LINE_COMMENTS(t):
    # Match and ignore comments
    #r'\/\*(\*(?!\/)|[^*])*\*\/'
    print("comments")
    print(t.value)
    return t


def t_COMMENTS(t):
    # Match and ignore comments
    # Just handling single line comments for now!
    #r'\/\*(\*(?!\/)|[^*])*\*\/'
    r"(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(//.*)"
    print("comments")
    print(t.value)
    return t
'''

def t_error(t):
    #print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

#t_ignore = " \t\n"


for i in range(len(x)):
	line = x[i]
	line = line.strip()
	y = re.findall("#define .+", line)
	if(y):
		y = y[0][8:]
		z = re.search("[a-zA-Z_][a-zA-Z_0-9]*", y)
		val = (y[z.end()+1:])
		macros[z.group()] = val
	else:
		#print(line)
		lexer = lex.lex()
		lexer.input(line)

		new_line = ""
		# Tokenize
		while True:
			lexer.input(line)
			tok = lexer.token()
			if not tok:
				break      # No more input
			#print(tok)
			'''
			if(tok.type == "COMMENTS"):
				#print("tok.pos = ", tok.lexpos)
				if(tok.lexpos != 0):
					new_line = line[:tok.lexpos] + " "
				else:
					new_line = " "
				break
			else:
				#print("tok.value = ", tok.value)
				new_line = line[:tok.lexpos] + macros[line[tok.lexpos]] + line[tok.lexpos+1:]
				line = new_line
			'''
			if(tok.type == "IDENTIFIER"):
				new_line = line[:tok.lexpos] + macros[line[tok.lexpos]] + line[tok.lexpos+1:]
				line = new_line
		#print(new_line == "")
		if(new_line):
			#print(new_line)
			#print(tok.lexpos)
			if(new_line != ""):
				o.write(new_line)
				o.write('\n')
		else:
			#print(line)
			if(line != ""):
				o.write(line)
				o.write('\n')

o.close()
