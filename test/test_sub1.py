import src.submodule1.sub1 as sub1, os
from src.submodule1.sub1 import requireInt

def test_simplest():
    assert requireInt() == 9

def test_static_true():
    assert sub1.TestClass1.staticReturnTrue()
    print('aboba')

def test_static_notTrue():
    assert not sub1.TestClass1.staticReturnFalse() and sub1.TestClass1.staticReturnTrue()

def test_true_obj():
    obj = sub1.TestClass1()
    value = obj.returnTrue()

    assert value

def test_false_obj():
    if 0==0:
        obj = sub1.TestClass1()
    else:
        obj = sub1.TestClass2()
        
    value = obj.returnFalse()

    assert not value

def test_test_test():
    obj = sub1.TestClass1.Subclass.alwaysTrue()
    var = requireInt()
    assert True