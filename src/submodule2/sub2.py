from src.submodule1.sub1 import TestClass1 as TC

class Submodule:

    variable = 0

    def __init__(self):
        self.variable = 1
        self.var2 = 2
        pass

    def returnVariable(self):
        return self.variable
    
    def changeVariable(self, value):
        self.var2 = value
        self.variable = value
        TC.staticReturnTrue()

def doNothing():
    pass