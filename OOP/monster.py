
class Monster(object):
	"""This calls initializes a monster with certain
	    attributes
	     """
	def __init__(self,**kwargs):
		"""All objects in python have the init method.
		    It sets attributes on creation. It uses a 
		    dictionary unpacking (**kwargs).
		 """
		self.hit_points = kwargs.get("hit_points", 1) 
		self.weapon = kwargs.get("weapon", "sword") 
		self.color = kwargs.get("color", "yellow") 
		self.sound = kwargs.get("sound", "ROAR") 



	def battlecry(self):
		return self.sound.upper()

