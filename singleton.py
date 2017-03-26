# class Singleton:
	# """Not the best way to implement the singleton design pattern"""
	# _instance = None
	# def __new__(self):
		# if not self._instance:
			# self._instance = super(Singleton, self).__new__(self)
			# self.y = 10
		# return self._instance
	# def setY(self, y):
		# self.y = y
	
# x = Singleton()
# print(x.y)
# x.setY(5)
# z = Singleton()
# print(z.y)

def singleton(my_class):
	"""Good way to implement the singleton design pattern (decorator)"""
	instances = {}
	def getInstance(*args, **kwargs):
		if my_class not in instances:
			instances[my_class] = my_class(*args, **kwargs)
		return instances[my_class]
	return getInstance
	
@singleton
class Monster:
	def __init__(self,strength=10,accuracy=10,defence=10,hp=100):
		self.strength = strength
		self.accuracy = accuracy
		self.defence = defence
		self.hp = hp
		
	def __str__(self):
		return (str(self.strength) + " " + str(self.accuracy) + " " +
				str(self.defence) + " " + str(self.hp)
				)
	
	def levelUp(self):
		self.strength *= 1.25
		self.accuracy *= 1.25
		self.defence *= 1.25
		self.hp *= 1.25
	
monster1 = Monster(20,10,20,80)
monster1.levelUp()
monster2 = Monster(15,15,15,120)
print(str(monster1))
print(str(monster2))