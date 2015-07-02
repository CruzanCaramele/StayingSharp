shopping_list = list() # [] could als be userd

print("what should we pick at the store? ")
print("Enter 'Done' to stop adding items.  ")

while True:
	new_item = raw_input("> ")

	if new_item == "DONE":
		break 
	shopping_list.append(new_item)
	print("Added list has {} items, ".format(len(shopping_list)))
	continue

print("Here's your list: ")


for item in shopping_list:
	print(item)