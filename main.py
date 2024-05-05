from s_lexer import lexer
from s_parser import parser
from s_intrepreter import Interpreter

# def main():
#     lexer.input("print 3")
#     for tok in lexer:
#         print(tok)
#     print(parser.parse("print 3"))

def main():
    while True:
        try:
            s = input('calc > ')
        except EOFError:
            break
        if not s: continue
        ast = parser.parse(s, lexer=lexer)
        interpreter = Interpreter()
        interpreter.visit(ast)

if __name__ == '__main__':
    main()
