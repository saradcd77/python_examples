
""" Splitting String and Printing in different line"""

string_example = "This is a string\nthis string will be printed in new line below\nthis one too"
# print(string_example)

""" Example of tabbed String"""

tabbed_string = "1\t2\t3\t4"
# print(tabbed_string)


"""String Slicing"""
				#           11111111112222 
				# 012345678901234567890123
				#				    -4-3-2-1
string_slicing = "Today is a beautiful day"

# Positive Slicing 
print('*'*20+' Positive Slicing  '+ '*'*20)

print(string_slicing[1:3]) #-> prints "od"
print(string_slicing[0:1]) #-> prints "T"
print(string_slicing[23]) #-> prints y
print(string_slicing[1:5]) #-> prints "oday"
print(string_slicing[:5]) #-> prints "Today" same as 0:5
print(string_slicing[6:]) #-> prints "is a beautiful day" prints from index 6 -> end of string
print(string_slicing[0:5]+string_slicing[5:]) #--> guess what will be printed?
print(string_slicing[:])  #prints the entire string
print(string_slicing[::]) #--> guess what will be printed?
print(string_slicing[1:5:2]) #--> prints "oa" (starts from 1st index to 4th, stepping every 2 indices)
print(string_slicing[0:5:3]) # --> prints "Ta" (starts from 1st index to 4th, stepping every 2 indices)

# Negative Slicing
# print('*'*20+' Negative Slicing '+ '*'*20)

print(string_slicing[-1:]) # --> Prints "y"
print(string_slicing[-4:-2]) #-> prints "d"
print(string_slicing[-4:22]) #-> prints "d"
print(string_slicing[-5:20]) #--> prints "l"
print(string_slicing[23:0:-1]) #--> prints "from end of string up to o"
print(string_slicing[23::-1]) # --> prints "from the end of string up to 0 index"
print(string_slicing[::-1]) #-> reverses the string (same as above)


"""String Replacement fields"""

age = 31
first_name = "Sarad"
last_name = "Dhungel"

print("Hi, My name is {} {} and I am {} years old".format(first_name, last_name, age))
print("Hi, My name is {0} {1} and I am {2} years old".format(first_name, last_name, age))

# Python 2 String Interpolation
print("Hi, My name is %s %s and I am %d years old"%(first_name, last_name, age))

# f-strings python 3.0 and above
print(f"Hi, My name is {first_name} {last_name} and I am {age} years old")



