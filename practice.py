a="hello"
print a
print(id(a))
a,b,c=5,3.2,"hello chchchchchchchchchchchchchchchcaaaaaaaaaaa"
print a,  b,  c
print(id(a))
print(id(c))
a=50
b=50
d=c
print(id(b))
print(id(a))
print(id(50))
print(id("hello"))
print(id(d))
print(id("hello chchchchchchchchchchchchchchchcaaaaaaaaaaaaaaaaa"))
print(type(c))
print(type(11))
print(d==c)

def f(v):
    print(v)
    return 12
print(type(f(1)))
print(id(12))
