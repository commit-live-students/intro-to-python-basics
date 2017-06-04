a="Hello"
print(a)
b=a
#a.lowercase()
print(a)

def f():
    """
    documentation of function
    """
    pass
print f.__doc__

#help(f)
#help([].append)
a=1
b=2
#print(a,b,c)
def swp():
    #print(a,b,c)
    c=a
    print(a,b,c)
    b=c
    print(a,b,c)
    a=b
    print(a,b,c)
swp()
print(a,b)
