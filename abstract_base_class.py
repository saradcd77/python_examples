# This example shows a simple use case of Abstract base class, Inheritance and Polymorphism

# The base class that inherits abstract base class in python needs to override it's method signature
# In this case read method is overriden in methods of classes that inherits Electric_Device
# Importing in-built abstract base class

from abc import ABC, abstractmethod

# Custom Exception
class InvalidOperationError(Exception):
	pass

# Inherits ABC class
class Electric_Device(ABC):

	def __init__(self):
		self.open = False

	def turn_on_device(self):
		if self.open:
			raise InvalidOperationError("Electric_Device is already ON!")

		self.open = True

	def turn_off_device(self):
		if not self.open:
			raise InvalidOperationError("Electric_Device is OFF")
		self.open = False

	@abstractmethod
	def charge(self):
		pass

class Heater(Electric_Device):

	def charge(self):
		print("Charging Electric Heater!")

class Kettle(Electric_Device):

	def charge(self):
		print("Charging Electric Kettle! ")


device1 = Kettle()
device1.charge()

device2 = Heater()
device2.charge()
device2.turn_on_device()
print(device2.open)
