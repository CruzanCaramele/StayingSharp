import sys
from character import Character 
from monster import Dragon 
from monster import Goblin 
from monster import Troll 


class Game(object):
	def setup(self):
		self.player = Character()
		self.monsters = [
		     Goblin(),
		     Troll(),
		     Dragon()
		]

		self.monster = self.get_next_monster()

	def get_next_monster(self):
		try:
			return self.monsters.pop(0)

		except IndexError:

			return None

	def monster_turn(self):
		"""Check to see if monster attack
		    If so, tell the player
		    Check if player wants to dodge,
		    if so see if dodge is successfull,
		    if so , move on 
		    if not, remove one player hit point
		    if the monster is attacking, tell the 
		    player as well
		"""
		if self.monster.attack():
			print("{} is attacking !".format(self.monster))

			if raw_input("Dodge ? Y/N").lower() == "y":
				if self.player.dodge():
					print("you dodged")
				else:
					print("you got hit")
					self.player.hit_points -= 1
			else:
				print("{} hit you for 1 point !".format(self.monster))
				self.player.hit_points  -= 1
		else:
			print ("{} is not attacking this turn".format(self.monster))


	def player_turn(slef):
		"""Let the player, attack, rest or quit
		    If player attacks: see if the attack 
		    is successfull, if so, see if the
		    monster dodges, If dodged, print
		    that. If not dodged, subtract the 
		    right num of hit points from the 
		    monster. If not a good attack, tell
		    the player.

		    if player resets, call player.rest()
		    if quit, exit the game,
		    if anythin else, re-run this method
		"""
		player_choice = raw_input("[A]ttack, [R]est, [Q]uit?").lower()
		if player_choice == "a": 
			print("You're attacking {}!".format(self.monster))

			if self.player.attack():
				if self.monster.dodge():
					print("{} dodged attack".format(self.monster()))
				else:
					if self.player.leveled_up():
						self.monster.hit_points -= 2
					else:
						self.monster. hit_points -= 1

					print ("You hit {} with {}".format(self.monster,
						self.player.weapon))
			else:
				print("You missed")

		elif player_choice == "r": 
			self.player.rest()
		elif player_choice == "q": 
			sys.exit()

		else:
			self.player_turn()


	def cleanup(self):
		"""If the monster has no more hit points,
		    up the player's experience, print a 
		    message, Get a new monster.
		"""
		if self.monster.hit_points <= 0: 
			self.player.experience += self.monster.experience
			print("you killed {}!".formatself.monster)
			self.monster = self.get_next_monster()


	def __init__(self):
		self.setup()

		while self.player.hit_points and (self.monster or self.monsters):
			print("\n'+'="*20)
			print (self.player)
			self.monster_turn()
			print("-"*20)
			self.player_turn()
			self.cleanup()
			print("\n'+'="*20)


		if self.player.hit_points:
			print("You win!")
		elif self.monsters or self.monster:
			print("You Lose!")
		sys.exit()

Game()
