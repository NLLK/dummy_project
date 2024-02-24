#import src.submodule1.sub1 as sub1

from src.submodule1 import sub1

def test_static_true():
    assert sub1.TestClass1.staticReturnTrue()

def test_static_notTrue():
    assert not sub1.TestClass1.staticReturnFalse()

def test_true_obj():
    obj = sub1.TestClass1()
    value = obj.returnTrue()

    assert value

def test_false_obj():
    obj = sub1.TestClass1()
    value = obj.returnFalse()

    assert not value
