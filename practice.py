l = []
l = range(2,101,2)
print l

#find all fibonacci sequence up to 10
l1 = []
a = 0
b = 1
l1.append(a)
l1.append(b)
for i in range(10):
    c = a+b
    l1.append(c)
    a = b
    b = c

print l1
