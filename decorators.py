def ruinFood(food_func):
	def addCremeFraiche():
		return food_func() + " with crème fraiche"
	return addCremeFraiche

def chickpeaTagine():
	return "chickpea tagine"

@ruinFood
def peanutSkittles():
	return "peanut butter and skittle sandwich"
	
food = ruinFood(chickpeaTagine)
print(food())
print(peanutSkittles())