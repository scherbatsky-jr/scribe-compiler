import ply.yacc as yacc
from s_lexer import tokens
from s_ast import NumNode, BinOpNode, PrintNode, VarAssignNode, VarAccessNode

def p_program(p):
    '''
    program : statement_list
    '''
    p[0] = p[1]

def p_statement_list(p):
    '''
    statement_list : statement_list statement SEMICOLON
                   | statement SEMICOLON
    '''
    if len(p) == 4:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement(p):
    '''
    statement : print_statement
              | assignment_statement
              | expression_statement
    '''
    p[0] = p[1]

def p_expression_paren(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_print_statement(p):
    'print_statement : PRINT LPAREN expression RPAREN'
    p[0] = PrintNode(p[3])

def p_expression_identifier(p):
    'expression : IDENTIFIER'
    p[0] = VarAccessNode(p[1])

def p_expression_statement(p):
    'expression_statement : expression'
    p[0] = p[1]

def p_assignment_statement(p):
    'assignment_statement : IDENTIFIER EQUALS expression'
    p[0] = VarAssignNode(p[1], p[3])

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = BinOpNode(p[1], '+', p[3])

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = BinOpNode(p[1], '-', p[3])

def p_expression_divide(p):
    'expression : expression DIVIDE term'
    p[0] = BinOpNode(p[1], '/', p[3])

def p_expression_times(p):
    'expression : expression TIMES term'
    p[0] = BinOpNode(p[1], '/', p[3])

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

# Ensure base cases for recursion:
def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_number(p):
    'factor : NUMBER'
    p[0] = NumNode(p[1])

def p_error(p):
    if p:
        print(f"Syntax error at token {p.type}, value '{p.value}' at line {p.lineno}")
    else:
        print("Syntax error at EOF")


parser = yacc.yacc(debug=True)
