num1 = 0
num2 = 1
list1 = [num1, num2]
for i in range(10):
    num3 = num1 + num2
    list1.append(num3)
    num1 = num2
    num2 = num3
print list1
