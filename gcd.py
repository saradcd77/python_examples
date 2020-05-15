""" The greatest denominator of two numbers using Euclid's Geometry"""
# Note: GCD is the largest positive integer that divides both given numbers without the reminder

def find_gcd(a, b):
	while (b != 0):
		temp = a
		a = b
		b = temp % a

	return a 


# Using recursion

def find_gcd(a, b):
	if b == 0:
		return a;
	else:
		return find_gcd(b, a % b)


print(find_gcd(20,4))
print(find_gcd(20,8))
print(find_gcd(60,96))
