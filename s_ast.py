class NumNode:
    def __init__(self, value):
        self.value = value

class BinOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class PrintNode:
    def __init__(self, value):
        self.value = value

class IfNode:
    def __init__(self, condition, then_branch, elif_branches=None, else_branch=None):
        self.condition = condition
        self.then_branch = then_branch
        self.elif_branches = elif_branches if elif_branches else []
        self.else_branch = else_branch

    def __repr__(self):
        return f"IfNode(condition={self.condition}, then_branch={self.then_branch}, elif_branches={self.elif_branches}, else_branch={self.else_branch})"


class WhileNode:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class RelationalNode:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right
        
class BoolNode:
    def __init__(self,value):
        self.value=value

class VarAssignNode:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class VarAccessNode:
    def __init__(self, name):
        self.name = name

    def execute(self, environment):
        environment[self.name] = self.value.execute(environment)
