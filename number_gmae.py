import random

rand_num = random.randint(1, 10)
guess_nums = []
allowed_guesses = 5

while len(guess_nums) < allowed_guesses:
	guess = raw_input("Guess a number betoween 1 and 10: ")

	try:
		player_num = int(guess)
	except:
		print("that's not a whole number! ")
		break

	if not player_num > 0 or not player_num < 11:
		print("Thats not betoween 1 and 10")
		break 

	#append user input to number of guesses
	guess_nums.append(player_num)

	if player_num == rand_num:
		print("You WIN!!! : My number was {} ".format(rand_num))
		print("Tries {} ".format(len(guess_nums)))
		break
	else:
             	if rand_num > player_num:
             		print("Nope guess higher, you are \
             			now on {} guess "
             			.format(len(guess_nums)))
             	else:
             		("Guess lower, guess are {} ". format(len(guess_nums)))
             	continue

if not rand_num in guess_nums:
	print("answer is {} ". format(rand_num))
