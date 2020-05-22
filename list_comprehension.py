""" Examples of usage of List Comprehension """

# Finding square of the numbers from 1 to 5

numbers = [1, 2, 3, 4, 5]
squares = []

# Using for-loop 
for number in numbers:
	squares.append(number ** 2)

print(squares)

# Using List comprehension

squares = [number ** 2 for number in numbers]
print(squares)


""" Another example. Regular way Vs List Comprehension """

# Finding the length of the string using regular for-loop

# Using regular for-loop
text = input("Please enter your text: ")
output = []
for x in text.split():
    output.append(len(x))
print(output)

# Using List Comprehension
output = [(x,len(x)) for x in text.split()]
print(output)

""" Condtional Comprehension or using Filter along with Comprehension """
output = [(x, len(x)) for x in text.split() if len(x) > 4 and len(x) < 7] # only prints the words whose lenghts is > 4 and < 7