class colors:
    purple = '\033[30m'
    green = '\033[32m'
    yellow = '\033[93m'
    grey = '\033[37m'
    red='\033[31m'

checklist = list()

# CREATE
def create(item):
        checklist.append(item)

# READ
def read(index):
    if in_scope(index):
        print(checklist[index])
        return checklist[index]
    else:
        print ("Index out of scope")

# UPDATE
def update(index, item):
    if in_scope(index):
        checklist[index] = item
    else:
        print("Index out of sccope")

# DESTROY
def destroy(index):
    if in_scope(index):
        checklist.pop(index)
    else:
        print("Index out of scope")

# LIST ALL ITEMS
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

# MARK COMPLETED
def mark_completed(index):
    if in_scope(index):
        update(index, ' √ ' + checklist[index])
    else:
        print("\nIndex out of scope")

def in_scope(index):
    try:
        checklist[int(index)]
        return True
    except:
        return False

# SELECT
def select(function_code):
    # Create item
    if function_code == "C" or function_code == "c":
        input_item = user_input("Input item: ")
        create(input_item)

    # Read item
    elif function_code == "R" or function_code == "r":
        item_index = int(user_input("Index Number? "))
        # Remember that item_index must actually exist or our program will crash.
        read(item_index)

    # Update
    elif function_code == "U" or function_code == "u":
        list_all_items()
        update_index = input('What list item (by assosciated index) would you like to update? : ')
        new_item = input("Input new value: ")
        update(int(update_index), new_item)
        print('\nHere is the updated list: \n')
        list_all_items()

    #Destroy
    elif function_code == "D" or function_code == "d":
        list_all_items()
        destroy_index = input('What list item (by assosciated index) would you like to destroy? : ')
        destroy(int(destroy_index))
        list_all_items()

    # Print all items
    elif function_code == "P" or function_code == "p":
        list_all_items()

    elif function_code == "M" or function_code == "m":
        completed_index = input("Which item would you like to mark completed (enter index): ")
        mark_completed(int(completed_index))
        print("Updated List:\n")
        list_all_items()
    
    #Quit
    elif function_code == "Q" or function_code == "q":
        #Where the loop stops
        return False

    # Catch all
    else:
        print("Unknown Option")
    return True

# USER INPUT
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

    print(colors.yellow, read(0))

    print("\nCreate Tests: \n")
    select("C") #create test
    select("C")
    select("C") 
    in_scope(0) #should pass
    print("in bounds")
    in_scope(5) #should fail (print out of bounds)
    print("\nRead Test: \n")
    select("R") #read test
    print("\nUpdate Test: \n")
    select("U") #update test
    print("\nDestroy Test: \n")
    select("D") #destroy test
    print("\nPrint All Test: \n")
    select("P") #print all test
    print("\nMark Complete Test\n")
    select("M")
    print("\nQuit Test: \n")
    select("Q") #quit test


def run():
    running = True
    print(colors.grey)
    while running:
        selection = user_input(
            "\nPress C to create list, R to read, U to update item, D to destroy, M to mark completed, P to print list, and Q to quit  ")
        running = select(selection)


print(colors.yellow, "Welcome to the Captian Rainbow Checklist!")

start_option = input("Would you like to run the TEST or the full APPLICATION? Enter t/a:  ")
if start_option == "t" or start_option == 'T':
    print(colors.green)
    test()
elif start_option == 'a' or start_option == "A":
    print(colors.grey)
    run()
else:
    print("\nInvalid response\nExiting software\n")
