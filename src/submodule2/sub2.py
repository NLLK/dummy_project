class Submodule:

    variable = 0

    def __init__(self):
        self.variable = 0
        pass

    def returnVariable(self):
        return self.variable
    
    def changeVariable(self, value):
        self.variable = value

def doNothing():
    pass