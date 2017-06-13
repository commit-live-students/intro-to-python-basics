import pandas as pd
a="hello how are you. How are things going on in your life ksdghxlcn xckxc,cnbxm ,.cbxm ,cnbl;xm .,dksflk'mlzxnlxm.sl"
b='hello how are you. How are things going on in your life ksdghxlcn xckxc,cnbxm ,.cbxm ,cnbl;xm .,dksflk\'mlzxnlxm.sl'
print (a)
print (id(a))
print id(b)

def foo():
    a='hello'
    return a

b = foo()
print b
