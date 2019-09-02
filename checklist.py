class colors:
    purple = '\033[30m'
    green = '\033[32m'
    yellow = '\033[93m'


print("Hello World")

checklist = list();

# CREATE
"""checklist = list();
checklist.append('Blue')
print(checklist)
checklist.append("orange")
print(checklist)"""

# CREATE
def create(item):
    checklist.append(item)


# READ
"""def read(index):
   item = checklist[index]
   return item"""

# READ
def read(index):
    return checklist[index]


# UPDATE
"""checklist = ['Blue', 'Orange']
checklist[1] = 'Cats'
print(checklist)"""

# UPDATE
def update(index, item):
    checklist[index] = item

#DESTROY
"""checklist = ['Blue', 'Cats']
checklist.pop(1)
print(checklist)"""

# DESTROY
def destroy(index):
    checklist.pop(index)

# LIST ALL ITEMS
def list_all_items():
    index = 0
    for list_item in checklist:
        print(str(index) + list_item)
        index += 1

# MARK COMPLETED
def mark_completed(index):
    print ('√' + checklist[index])

# SELECT
def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number?")

        # Remember that item_index must actually exist or our program will crash.
        read(item_index)

    # Print all items
    elif function_code == "P":
        list_all_items()

    # Catch all
    else:
        print("Unknown Option")

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

# TEST
def test():
    create("purple sox")
    create("red cloak")

    print(colors.green, read(0))
    print(colors.green, read(1))

    update(0, "purple socks")
    destroy(1)

    print(colors.green, read(0))
    #print(read(1))

    select("C")

    list_all_items()

    select("R")

    list_all_items()

    user_value = user_input("Please Enter a value:")
    print(user_value)

test()