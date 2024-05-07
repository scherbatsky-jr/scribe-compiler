import ply.lex as lex

tokens = (
    'NUMBER', 'IDENTIFIER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS',
    'LPAREN', 'RPAREN', 'PRINT', 'SEMICOLON', 'LBRACE', 'RBRACE',
    'GT', 'GTE', 'LT', 'LTE', 'EQUAL', 'NOTEQUAL',
    'IF', 'ELSE', 'WHILE','TRUE','FALSE','BOOL', 'ELIF'
)

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_PRINT   = r'print'
t_SEMICOLON = r';'
t_GT = r'>'
t_GTE = r'>='
t_LT = r'<'
t_LTE = r'<='
t_EQUAL = r'=='
t_NOTEQUAL = r'!='
t_LBRACE = r'\{'
t_RBRACE = r'\}'

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'print': 'PRINT',
    'true':'BOOL',
    'false':'BOOL',
    'elif': 'ELIF'
}

t_ignore = ' \t'

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_BOOL(t):
    r'\btrue\b|\bfalse\b'
    t.value = True if t.value == 'true' else False
    t.type = 'BOOL'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
