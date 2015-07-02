shopping_list = []

def show_help():
	"""instructions to user"""
	print("what should we pick at the store? ")
	print("Enter 'DONE' to stop adding items.  ")
	print("Enter 'HELP' for help.  ")

def add_to_list(item):
	"""append item or items to shopping_list supplied by user"""
	shopping_list.append(item)
	print("Added: list has {} items ".format(len(shopping_list)))


def show_list():
	"""show the shopping_list"""
	print("here's your list")

	for item in shopping_list:
		print(item)

show_help()

while True:
	new_item = raw_input("> ")

	if new_item == "DONE":
		break 

	elif new_item == "HELP":
		show_help()
		continue
		
	elif new_item == "SHOW":
		show_list()
		continue

	add_to_list(new_item)
	continue 

show_list()
