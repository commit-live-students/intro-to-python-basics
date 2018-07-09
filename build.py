''' Even number between 1 and 100'''
i=1
while i <= 100:
	if i%2 == 0:
		print i
	i=i+1
# Generate Fibonacci series upto 10

a,b = 0,1
print a,b
for i in range(0,15):
	c = a+b
	a,b=b,c
	print c
