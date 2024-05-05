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

class VarAssignNode:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class VarAccessNode:
    def __init__(self, name):
        self.name = name
