'''With a given integral number n, write a function to generate a dictionary that contains (i, i*i)
 such that is an integral number between 1 and n (both included).

    Number should not be less than 0 and should not be greater than 100.
    Calculate square of all number from 1 to n and store in dict.
    Function should pass all test cases '''

x = input ( " Enter a number between 0 and 100: ")
if x <= 0 or x > 100:
	print "Number invalid"
else :
	S = {item:item*item for item in range(x)}
print S
