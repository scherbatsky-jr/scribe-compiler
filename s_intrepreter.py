from s_ast import NumNode, BinOpNode, PrintNode, VarAssignNode, VarAccessNode

class Interpreter:
    def __init__(self):
        self.environment = {}

    # def visit(self, node):
    #     if isinstance(node, NumNode):
    #         return self.visit_NumNode(node)
    #     elif isinstance(node, str):  # Handling strings directly if they slip through
    #         return node
    #     elif isinstance(node, int):
    #         return node
    #     else:
    #         method_name = 'visit_' + type(node).__name__
    #         visitor = getattr(self, method_name, self.generic_visit)
    #         return visitor(node)

    def visit(self, node):
        # Check if the node is a list of nodes and handle each item in the list
        if isinstance(node, list):
            return [self.visit(item) for item in node]

        # Return the value directly if the node is a basic type (int, str)
        # This avoids unnecessary method calls for simple types
        if isinstance(node, (int, str, float)):
            return node

        # Dispatch to the appropriate visit method based on the type of node
        if isinstance(node, NumNode):
            return self.visit_NumNode(node)

        # For all other types, use reflection to find the appropriate method
        else:
            method_name = 'visit_' + type(node).__name__
            visitor = getattr(self, method_name, self.generic_visit)
            return visitor(node)

    def visit_NumNode(self, node):
        return node.value

    def visit_BinOpNode(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        
        # type check both nodes before operation
        if type(left) != type(right):
            raise TypeError(f"Cannot perform '{node.op}' between types {type(left).__name__} and {type(right).__name__}")

        op = node.op
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '/':
            if right == 0:
                raise ZeroDivisionError("division by zero")
            return left / right
        else:
            raise ValueError(f"Unknown operator {op}")
        
    def visit_PrintNode(self, node):
        value = self.visit(node.value)
        print(value)
        return value

    def visit_VarAssignNode(self, node):
        value = self.visit(node.value)
        self.environment[node.name] = value
        return value
        print(f"Assigned {node.name} = {self.environment[node.name]}")

    def visit_VarAccessNode(self, node):
        name = node.name
        if name in self.environment:
            return self.environment[name]
        else:
            raise NameError(f"Variable '{name}' not defined")
        
    def visit_IfNode(self, node):
        if self.visit(node.condition):
            return self.visit(node.then_branch)
        else:
            for condition, branch in node.elif_branches:
                if self.visit(condition):
                    return self.visit(branch)
            if node.else_branch:
                return self.visit(node.else_branch)

    
    def visit_WhileNode(self, node):
        while self.visit(node.condition):
            self.visit(node.body)

    def visit_RelationalNode(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        if node.operator == '>':
            return left > right
        elif node.operator == '>=':
            return left >= right
        elif node.operator == '<':
            return left < right
        elif node.operator == '<=':
            return left <= right
        elif node.operator == '==':
            return left == right
        elif node.operator == '!=':
            return left != right
        
    def visit_BoolNode(self,node):
        return node.value

    def visit_Block(self, node):
        for stmt in node.statements:
            self.visit(stmt)


    def visit_list(self, nodes):
        return [self.visit(node) for node in nodes]

    def generic_visit(self, node):
        raise Exception(f'No visit_{type(node).__name__} method')
