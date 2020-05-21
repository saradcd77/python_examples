import sys

def gen_range(n:int):
    print("gen_range_starts")
    start = 0
    while start < n:
        print("gen_range is returning {}".format(start))
        start += 1
        yield start

print(list(gen_range(5)))
print(sys.getsizeof(gen_range(5))) #--> shows the size used by the function gen_range

# Fibonacci sequence
def fibonacci():
    current, previous = 0, 1
    while True:
        yield current
        current, previous = current + previous, current


fib = fibonacci()
for i in range(10):
    print(next(fib))
