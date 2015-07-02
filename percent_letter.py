user_string = raw_input("whats your word ? ")
user_num = raw_input("whats your number ? ")

try:
	"""check to turn number to integer else a float"""
	our_num = int(user_num)
except:
	our_num = float(user_num)

if not "." in user_num:
	print(user_string[our_num])
else:
	#round float to neareat whole number
	ratio = round(len(user_string)*our_num)
	print ratio
	print(user_string[int(ratio)])