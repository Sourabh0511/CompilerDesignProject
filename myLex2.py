import ply.lex as lex
from ply.lex import TOKEN
import sys

class MyLexer(object):

    # List of token names.   This is always required
    keywords =  [
                    'break',
                    'return',
                    'continue',
                    'long',
                    'unsigned',
                    'signed',
                    'double',
                    'class',
                    'private',
                    'protected',
                    'public',
                    'int',
                    'main',
                    'while',
                    'if',
                    'else',
                    'char',
                    'short',
                    'float',
                    'void',
                    'cout'
                ]
    tokens =       (
                    'identifier',
                    'pipe_pipe',
                    'ampersand_ampersand',
                    'equal',
                    'star_equal',
                    'slash_equal',
                    'mod_equal',
                    'plus_equal',
                    'minus_equal',
                    'left_shift_equal',
                    'right_shift_equal',
                    'ampersand_equal',
                    'cap_equal',
                    'pipe_equal',
                    'notequal',
                    'equal_equal',
                    'lt',
                    'gt',
                    'lte',
                    'gte',
                    'left_shift',
                    'right_shift',
                    'arrow',
                    'plus_plus',
                    'minus_minus',
                    'colon_colon',
                    'integer_constant',
                    'character_constant',
                    'floating_constant',
                    'string_literal',
                    'l_paren',
                    'r_paren',
                    'colon',
                    'l_brace',
                    'r_brace',
                    'semicolon',
                    'comma',
                    'question_mark',
                    'pipe',
                    'cap',
                    'ampersand',
                    'plus',
                    'minus',
                    'slash',
                    'star',
                    'mod',
                    'exclamation',
                    'tilde',
                    'r_bracket',
                    'dot',
                    'l_bracket',
                    'new_line',
                    'Break',
                    'Return',
                    'Continue',
                    'Long',
                    'Unsigned',
                    'Signed',
                    'Double',
                    'Class',
                    'Private',
                    'Protected',
                    'Public',
                    'Int',
                    'Main',
                    'While',
                    'If',
                    'Else',
                    'Char',
                    'Short',
                    'Float',
                    'Void',
                    'Cout'
                )

    # Regular expression rules for simple tokens

    t_pipe_pipe                     = r'\|\|'
    t_ampersand_ampersand           = r'&&'
    t_equal_equal                   = r'=='
    t_equal                         = r'='
    t_star_equal                    = r'\*='
    t_slash_equal                   = r'/='
    t_mod_equal                     = r'%='
    t_plus_equal                    = r'\+='
    t_minus_equal                   = r'-='
    t_left_shift_equal              = r'<<='
    t_right_shift_equal             = r'>>='
    t_ampersand_equal               = r'&='
    t_cap_equal                     = r'\^='
    t_pipe_equal                    = r'\|='
    t_notequal                      = r'!='
    t_lte                           = r'<='
    t_gte                           = r'>='
    t_left_shift                    = r'<<'
    t_right_shift                   = r'>>'
    t_lt                            = r'<'
    t_gt                            = r'>'
    t_minus_minus                   = r'\-\-'
    t_arrow                         = r'->'
    t_plus_plus                     = r'\+\+'
    t_colon_colon                   = r'::'
    t_character_constant            = r'\"[a-zA-Z]\"'
    t_floating_constant             = r'[0-9]+\.[0-9]+'
    t_l_paren                       = r'\('
    t_r_paren                       = r'\)'
    t_colon                         = r':'
    t_l_brace                       = r'{'
    t_r_brace                       = r'}'
    t_semicolon                     = r';'
    t_comma                         = r','
    t_question_mark                 = r'\?'
    t_pipe                          = r'\|'
    t_cap                           = r'\^'
    t_ampersand                     = r'&'
    t_plus                          = r'\+'
    t_minus                         = r'-'
    t_slash                         = r'/'
    t_star                          = r'\*'
    t_mod                           = r'%'
    t_exclamation                   = r'!'
    t_tilde                         = r'~'
    t_r_bracket                     = r']'
    t_dot                           = r'\.'
    t_l_bracket                     = r'\['
    #t_at                            = r'@'
    #t_string_literal                = r'[a-zA-Z0-9_ ]+'
    # A regular expression rule with some action code
    # Note addition of self parameter since we're in a class


    def t_integer_constant(self,t):
        r'[0-9]+'
        t.value = int(t.value)
        return t

    def t_string_literal(self, t):
        #r'@[^"\n]*@$'
        #r'[@][a-zA-Z_][a-zA-Z0-9_]*[@]'
        r'@@[a-zA-Z0-9_ ]+@@'
        t.value = str(t.value)
        return t

    def t_identifier(self, t):
        # This checks if the lexeme is an identifier or a keyword and returns accordingly
        r'[a-zA-Z_][a-zA-Z0-9_]*'

        if(t.value in (self.keywords)):
            t.type = t.value[0].upper() + t.value[1:]

        return(t)

    # Define a rule so we can track line numbers
    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'

    # Error handling rule
    def t_error(self,t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Build the lexer
    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # Test it output
    def test(self,data):
        self.lexer.input(data)
        while True:
             tok = self.lexer.token()
             if not tok:
                 break
             print(tok)

def p_error():
    print("Syntax Error")

# create the lexer
m = MyLexer()

# Build the lexer
m.build()


if __name__ == "__main__":
    # Build the lexer and try it out
    # m = MyLexer()

    # Build the lexer
    # m.build()

    with open(sys.argv[1], "r") as f:
        data = f.read().strip()


    print("C++ CODE\n")
    print(data)
    print("\n")
    print("TOKENS\n\n")
    m.test(data)     # Test it
