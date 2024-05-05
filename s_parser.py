import ply.yacc as yacc
from s_lexer import tokens
from s_ast import NumNode, BinOpNode, PrintNode, VarAssignNode, VarAccessNode, IfNode, WhileNode, RelationalNode,BoolNode

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
              | if_statement
              | while_statement
    '''
    p[0] = p[1]

def p_block(p):
    'block : LBRACE statement_list RBRACE'
    p[0] = p[2]

def p_relational_expression(p):
    '''
    expression : expression GT expression
               | expression GTE expression
               | expression LT expression
               | expression LTE expression
               | expression EQUAL expression
               | expression NOTEQUAL expression
    '''
    p[0] = RelationalNode(p[1], p[2], p[3]) 

def p_expression_paren(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_print_statement(p):
    'print_statement : PRINT LPAREN expression RPAREN'
    p[0] = PrintNode(p[3])

def p_expression_identifier(p):
    'expression : IDENTIFIER'
    p[0] = VarAccessNode(p[1])

def p_expression_binary(p):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
    '''
    if p[2] == '+':
        p[0] = BinOpNode(p[1], p[2], p[3])
    elif p[2] == '-':
        p[0] = BinOpNode(p[1], p[2], p[3])
    elif p[2] == '*':
        p[0] = BinOpNode(p[1], p[2], p[3])
    elif p[2] == '/':
        p[0] = BinOpNode(p[1], p[2], p[3])

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

def p_if_statement(p):
    '''
    if_statement : IF LPAREN expression RPAREN block
                 | IF LPAREN expression RPAREN block ELSE block
    '''
    if len(p) == 6:
        p[0] = IfNode(p[3], p[5])
    else:
        p[0] = IfNode(p[3], p[5], p[7])

def p_while_statement(p):
    'while_statement : WHILE LPAREN expression RPAREN block'
    p[0] = WhileNode(p[3], p[5])


# Ensure base cases for recursion:
def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_expression_boolean(p):
    'expression : BOOL'
    p[0] = BoolNode(p[1])

# def p_term_factor(p):
#     '''
#     term : factor
#          | term TIMES factor
#          | term DIVIDE factor
#     '''
#     if len(p) == 2:
#         p[0] = p[1]
#     elif p[2] == '*':
#         p[0] = BinOpNode(p[1], '*', p[3])
#     elif p[2] == '/':
#         p[0] = BinOpNode(p[1], '/', p[3])


# def p_factor_number(p):
#     '''
#     factor : NUMBER
#            | IDENTIFIER
#            | LPAREN expression RPAREN
#     '''
#     if isinstance(p[1], NumNode) or isinstance(p[1], VarAccessNode):
#         p[0] = p[1]
#     else:
#         p[0] = p[2]  # for expressions in parentheses

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
