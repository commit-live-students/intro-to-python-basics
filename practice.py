print list(range(0,100,2))

num1 = 0
num2 = 1
list = [num1, num2]
for num in range(10):
    num = num1 + num2
    list.append(num)
    num1, num2 = num2, num

print list
