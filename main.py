from s_lexer import lexer
from s_parser import parser
from s_intrepreter import Interpreter
from flask import Flask, render_template, request
from io import StringIO
import sys

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        code = request.form['code']
        processed_code = code.replace('\n', ' ').replace('\r', ' ')

        output = StringIO()           # Create a StringIO object to capture output
        sys.stdout = output           # Redirect stdout to the StringIO object

        try:
            # Parsing and interpreting the code
            ast = parser.parse(processed_code, lexer=lexer)
            interpreter = Interpreter()
            interpreter.visit(ast)
        except Exception as e:
            output.write(str(e))      # In case of errors in parsing or execution

        # Reset stdout to its original state
        sys.stdout = sys.__stdout__
        
        # Get the string from StringIO object
        output_str = output.getvalue()
        return render_template('index.html', code=code, output=output_str)
    return render_template('index.html', code='', output='')

if __name__ == '__main__':
    app.run(debug=True)

