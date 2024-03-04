import src.submodule1.sub1  as sub1
#import submodule2

from src.submodule2.sub2 import Submodule, doNothing

def test():
    if sub1.TestClass1.staticReturnTrue():
        print('good')
    else: print('wtf?')

    variable = sub1.TestClass1()

    if variable.returnEquals(1,1):
        print('ok')
    else: print('wtf????')

    # submodule2. ... idk how to use it anyway

    doNothing()

    var2 = Submodule()
    var2.changeVariable(1)

    if variable.returnEquals(1,var2.returnVariable()):
        print('okay')
    else: print('why')

test()