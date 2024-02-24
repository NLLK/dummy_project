from src.submodule1 import sub1

from src.submodule2.sub2 import Submodule, doNothing

def test_1():
    assert sub1.TestClass1.staticReturnTrue()

def test_2():
    variable = sub1.TestClass1()

    assert variable.returnEquals(1,1)

def test_3():
    doNothing()

    var2 = Submodule()
    var2.changeVariable(1)

    variable = sub1.TestClass1()

    assert variable.returnEquals(1,var2.returnVariable())

