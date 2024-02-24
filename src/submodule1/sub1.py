class TestClass1:

    class Subclass:
        def alwaysTrue(self):
            return True
        pass

    def __init__(self):
        self.aboba = 'aaa'
        pass

    def returnTrue(self):
        return True

    def returnFalse(self):
        return False

    @staticmethod
    def staticReturnTrue():
        return bool(0 == 0)
        return True

    @staticmethod
    def staticReturnFalse():
        return False

    @staticmethod
    def returnEquals(op1, op2):
        return op1 == op2

    pass