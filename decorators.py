def ruinFood(food_func):
	def addCremeFraiche(*args, **kwargs):
		return food_func(*args, **kwargs) + " with crème fraiche"
	return addCremeFraiche

def chickpeaTagine():
	return "chickpea tagine"

@ruinFood
def peanutSkittles():
	return "peanut butter and skittle sandwich"
	
@ruinFood
def anyFood(food="pasta primavera"):
	return food
	
food = ruinFood(chickpeaTagine)
print(food())
print(peanutSkittles())
print(anyFood("waffle fries"))