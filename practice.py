a= "Hello, this is the test exercise"
print a

#Comparing memory alloation blocks of strings in python
s1= "qwerty"
s2= "qwerty"
def printstring():
    print "string 1 is: ", s1
    print "string 2 is: ", s2
printstring()

def printid():
    print "id of string 1 is: ", id(s1)
    print "id of string 2 is: ", id(s2)
    global ids2
    ids1= id(s1)
    ids2= id(s2)
    print "this is calling the local variable ids1 for id of s1", ids1
printid()

print "this is calling the global variable ids2 for id of s2", ids2

print "if id of s1 and s2 are the same, memory alloc is a match"

print "type() function is used to view the type of the variable defined"
n1= 12345
print "value of n1 is", n1
print "type of the n1 variable is", type(n1)

def lists():
   print "lists are a data structure in python"
   print "lists in python are heterogeneous, they house various datatypes"
   a= [1,2,3,"aaaaa"]
   print a
   print (a, "is of type", type(a))
lists()

def dictionary():
   print "dictionaries are a data structure in python"
   print "dictionaries are represented as 'dict' "
   a= {"big data" : "data"}
   print a
   print (a, "is of type", type(a))
dictionary()

def append():
    print "demonstrating append for lists"
    l=[1,2,3,4]
    print l
    l.append(5)
    print l
append()

def importing():
    print "to import math library, type 'import math'"
    import math
    print "type of math library is", type(math)
    print (math.sqrt(16))
importing()

print """use tripple double quotes to write multiline strings,
Just like this!"""

string= "test case for strings"
print "characters form index 1 to -5: ", (string[1:-5])
print (len(string))
