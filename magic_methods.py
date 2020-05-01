class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
     	self.dict = {"a":1,"b":2}

    Return the attributes of the class using inbuilt string method
    def __str__(self):
        return f"({self.x},{self.y})"

    def __getitem__(self,key):
    	return self.dict[key]

    # Compares two object using inbuilt method greater than
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    # Compares two object using inbuilt method greater than
    def __le__(self, other):
        return self.x < other.x and self.y < other.y

point = Point(1, 2)
other = Point(3, 4)

print(point < other) #Prints True
print(other > point ) #Prints True
print(point) #Prints value of point object (1,2)

print(point.__getitem__("a")) # returns value of a i.e 1
print(point.__getitem__("d")) # Key error