import random
from combat import Combat

COLORS = ["yellow", "red", "blue", "green"]

class Monster(Combat):
	"""This calls initializes a monster with certain
	    attributes
	"""
	min_hit_points  = 1
	max_hit_points  = 1
	min_experience = 1
	max_experience = 1
	weapon = "sword"
	sound = "roar"


	def __init__(self,**kwargs):
		"""All objects in python have the init method.
		    It sets attributes on creation. It uses a 
		    dictionary unpacking (**kwargs).
		"""
		self.hit_points = random.randint(self.min_hit_points, 
			                                    self.max_hit_points)

		self.experience = random.randint(self.min_experience, 
			                                      self.max_experience)

		self.color = random.choice(COLORS)

		for key, value in kwargs.items():
			setattr(self, key, value)
		
		
		"""
		self.hit_points = kwargs.get("hit_points", 1) 
		self.weapon = kwargs.get("weapon", "sword") 
		self.color = kwargs.get("color", "yellow") 
		self.sound = kwargs.get("sound", "ROAR") 
		"""


	def __str__(self):
		"""This mehtod is called whenever any string
		    conversion takes place
		"""
		return "{} {}, HP: {}, XP: {}".format(self.color.title(),
			                                        self.__class__.__name__,
			                                        self.hit_points,
			                                        self.experience)


	def battlecry(self):
		return self.sound.upper()


class Goblin(Monster):
	max_hit_points  = 3
	max_experience = 2
	sound = "squeak"


class Troll(Monster):
	min_hit_points = 3
	max_hit_points = 5
	min_experience = 2
	max_experience = 6
	sound = "growl"


class Dragon(Monster):
	min_hit_points = 5
	max_hit_points = 10
	min_experience = 6
	max_experience = 10
	sound = "raaaar"


