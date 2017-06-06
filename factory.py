"""factory design pattern stuff"""

class Dessert:
	@classmethod
	def isHealthy(self):
		return False
		
print(Dessert.isHealthy())