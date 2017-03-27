"""type class creation (dynamic; can be good idea for short classes)"""

def initialize(self):
	self.toppings = []

def servePizza(self):
	if not self.toppings and self.noPizza:
		print("Your first pizza is here, it's a cheese pizza!")
		self.noPizza = False
	elif not self.toppings:
		print("You've already been served this cheese pizza!")
	elif self.noPizza:
		print("Your first pizza is here, it's got delicious toppings!")
		self.noPizza = False
	else:
		print("You've already been served this pizza with toppings!")
		
def addTopping(self, topping):
	self.toppings.append(topping)

# NOTE: noPizza is a class variable NOT an instance variable	
Pizza = type("Pizza", (object,),{"noPizza":True, "__init__":initialize,
								 "serve":servePizza, "addTopping":addTopping})

pizza1 = Pizza()
pizza1.serve()
pizza1.addTopping("mushrooms")
pizza1.serve()
pizza2 = Pizza()
pizza2.addTopping("mushrooms")
pizza2.serve()
