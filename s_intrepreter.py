from s_ast import NumNode, BinOpNode, PrintNode, VarAssignNode, VarAccessNode

class Interpreter:
    def __init__(self):
        self.environment = {}

    def visit(self, node):
        if isinstance(node, NumNode):
            return self.visit_NumNode(node)
        elif isinstance(node, str):  # Handling strings directly if they slip through
            return node
        elif isinstance(node, int):
            return node
        else:
            method_name = 'visit_' + type(node).__name__
            visitor = getattr(self, method_name, self.generic_visit)
            return visitor(node)

    def visit_NumNode(self, node):
        return node.value

    def visit_BinOpNode(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        if node.op == '+':
            return left + right
        elif node.op == '-':
            return left - right
        elif node.op == '*':
            return left * right
        elif node.op == '/':
            return left / right

    def visit_PrintNode(self, node):
        value = self.visit(node.value)
        print(value)
        return value

    def visit_VarAssignNode(self, node):
        self.environment[node.name] = self.visit(node.value)

    def visit_VarAccessNode(self, node):
        return self.environment.get(node.name, None)
    
    def visit_list(self, nodes):
        return [self.visit(node) for node in nodes]

    def generic_visit(self, node):
        raise Exception(f'No visit_{type(node).__name__} method')
