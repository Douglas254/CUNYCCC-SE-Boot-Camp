# from tracemalloc import start
# from jmespath import search


# PART A QUIZ
from doctest import Example


myList = [1,2,3,4,5,6,7,8]
myList2 = myList
myList2.insert(4,20)
print(myList,myList2)  # [1, 2, 3, 4, 5, 6, 7, 8] [1, 2, 4, 5, 20, 6, 7, 8]
del myList2[2]
print(myList2) # [1, 2, 4, 5, 20, 6, 7, 8]
myList3 = myList2
print(myList,myList2,myList3) # [1, 2, 4, 5, 6, 7, 8] [1, 2, 4, 5, 20, 6, 7, 8] [1, 2, 4, 5, 20, 6, 7, 8]


# PART B 
# count(sub,[start,[end]]) 
# sub - substring to be searched 
# start - search starts from this index 
# end - search ends from this index 
# example 
str = "string"
sub = "i";
print ("str.count(sub, 1, 8) : ", str.count(sub, 1, 8))
sub = "wow";
print( "str.count(sub) : ", str.count(sub))

# endswith(suffix,[start,[end]]) 
# endswith - method returns true if the string ends with the specified value otherwise false 
# start - starts search 
# end - ends search 
# surfix - can be string or tuple to look for 
# example 
str = "this is string example....wow!!!";

suffix = "wow!!!";
print( str.endswith(suffix))
print (str.endswith(suffix,20))

suffix = "is";
print (str.endswith(suffix, 2, 4))
print (str.endswith(suffix, 2, 6))

# find/index(sub,[start,[end]])  
# sub - substring to be searched 
# start - search starts from this index 
# end - search ends from this index 
# example 
stringSample    = "pecan pie"
substr          = "pie"
pos             = stringSample.find(substr)
print("'{}' was found in '{}' at position:{}".format(substr, stringSample, pos))
stringSample    = "elvis presley"
substr          = "presley"
pos             = stringSample.find(substr)
print("'{}' was found in '{}' at position:{}".format(substr, stringSample, pos))
stringSample    = "its now or never"
substr          = "or"
pos             = stringSample.find(substr,5,len(stringSample))
print("'{}' was found in '{}' at position:{}".format(substr, stringSample, pos))

# join()
# () elements are put here to be joined 
# Example
s = "-"
seq = ("a", "b", "c") 
print (s.join( seq ))

# replace(old,new[,count])
# old - value to be searched 
# new - replaced value 
# count - specifies how many occurences i want to replace
# Example
txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three",7)

print(x)

# split([sep[,maxsplit]]) 
# sep - this is the deliminator 
# Example
s = 'Python is Nice'

str_list = s.split(sep=' ', maxsplit=1)
print(str_list)

# splitlines([keepends])
# splitlines - method splits a string into a list.
# keepends Returns a list of the lines in the string, breaking at line boundaries. 
# Example
string1 = "Tim\nCharlie\nJohn\nAlan"
string2 = "Welcome\n\nto\r\nAskPython\t!"
string3 = "Keyboard\u2028Monitor\u2029\x1cMouse\x0cCPU\x85Motherboard\x1eSpeakers\r\nUPS"
 

print(string1.splitlines(keepends=True))
print(string2.splitlines(keepends=True))
print(string3.splitlines(keepends=True))

# startswith(prefix[,start[,end]]) 
# surfix - can be string or tuple to look for 
# start the method starts looking for the prefix
# end - ends looking for prefix
# Example
s = 'Make it work, make it right, make it fast.'
result = s.startswith('make', 14)
print(result)

# strip([chars]) 
# strip - removes any leading whitespace from string 
# Example
greeting = "     Hello!  "

stripped_greeting = greeting.strip()

print(stripped_greeting,"How are you?")


# PART C 
def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

# calling function 
is_prime(2) # True

is_prime(8) # False


# PART D 
def disStuInfo(schoolID,*firstName,**lastEmail):
    print(schoolID, firstName,lastEmail)
    for key, value in lastEmail.items():
        print("{} is {}".format(key,value))

print(disStuInfo(1001,"douglas","douglasobara97@gmail.com"))