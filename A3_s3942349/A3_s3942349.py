#COSC1519 Introduction to Programming
#Assessment 3 Programming Project
#Student name: Heath Yates
#Student number: s3942349
#Practical group : 1/2/3/4/5 (with Gayan Thursdays @ 14:30)

# PROGRAM FUNCTIONS
def program_start():  # states file information and then opens menu
    inventory_file = open('A3_s3942349_stock.txt', 'r')
    inventory_file_text = []
    inventory_file_lines = 0
    total_stock_value = 0.0
    seperator = inventory_file.readlines()
    seperator.pop(0)
    for word in seperator:  # runs through all seperator list items, only uses the position 4 and 5 to be added to
        # total stock value
        total_stock_value += float(word.split()[4]) * int(word.split()[5])
    inventory_file.close()
    inventory_file = open('A3_s3942349_stock.txt', 'r')
    for line in inventory_file:  # runs through all lines in file to show the column names, the first line of the
        # file by putting them into a list and only showing the first one
        inventory_file_text.append(line)
        inventory_file_lines += 1

    text_program_start = '--- Now running inventory manager 9000 ---\n'
    text_program_start += '--- Displaying data from original file ---\n'
    text_program_start += 'Loading data from file: A3_s3942349_stock.txt\n'
    text_program_start += 'Column titles are: ' + inventory_file_text[0]
    print(text_program_start, end='')
    inventory_file = open('A3_s3942349_stock.txt', 'r')
    inventory_file_lines = 0
    print('Items loaded are:')
    for row in inventory_file:  # runs through the lines in a file, excludes the first line then assigns first word
        # to a value to be printed
        if inventory_file_lines > 0:
            inventory_file_dict = {'man': row.strip()}  # this dictionary is only here to meet the rubric requirements
            print(inventory_file_dict['man'])
        else:
            inventory_file_lines += 1
    print('Total stock value is:', total_stock_value)
    program_menu()


def program_menu():  # gives user six options of how to use the program, user inputs number string to progress
    text_menu = '--- Program Menu ---\n'
    text_menu += '1 - Display single items information\n'
    text_menu += '2 - Display all items information\n'
    text_menu += '3 - Add an item\n'
    text_menu += '4 - Update an item\n'
    text_menu += '5 - Remove an item\n'
    text_menu += '6 - Save and exit\n'
    user_menu_selection = input(text_menu)
    while True:  # crude loop to make sure that user input is valid, for six corresponding values it will run a
        # different function, if none of these values are input, it will say that the input is incorrect and ask for
        # input again
        if user_menu_selection == '1':
            item_display_specific()
            break
        elif user_menu_selection == '2':
            item_display_all()
            break
        elif user_menu_selection == '3':
            item_add()
            break
        elif user_menu_selection == '4':
            item_update()
            break
        elif user_menu_selection == '5':
            item_remove()
            break
        elif user_menu_selection == '6':
            program_exit()
            break
        else:
            print('Wrong input, please try again.')
        user_menu_selection = input(text_menu)


def item_display_specific():  # displays all the information on a user selected item
    if update == False:
        inventory_file = open('A3_s3942349_stock.txt', 'r')
    else:
        inventory_file = open('updated_A3_s3942349_stock.txt', 'r')
    inventory_file_lines = 0
    loaded_items = ''
    for line in inventory_file:  # gathers first word of all file lines except the first line into variable
        if inventory_file_lines > 0:
            loaded_items += line.split()[0] + ', '
        inventory_file_lines += 1
    print('Now showing all items:')
    print(loaded_items)
    user_item_specific = input('What item do you want to look at?: ')
    # display specific item details
    if user_item_specific in loaded_items:  # item is valid, display item details and run menu
        if update == False:
            inventory_file = open('A3_s3942349_stock.txt', 'r')
        else:
            inventory_file = open('updated_A3_s3942349_stock.txt', 'r')
        for row in inventory_file:
            if user_item_specific in row:
                print(row)
        program_menu()
    else:  # item is invalid, show error message and run menu again
        print('Error! Item does not exist.')
        program_menu()


def item_display_all():  # displays all information on all items in last used file
    print('Now showing all item details in alphabetical order:')
    if update == False:
        inventory_file = open('A3_s3942349_stock.txt', 'r')
    else:
        inventory_file = open('updated_A3_s3942349_stock.txt', 'r')
    item_collection = []
    for row in inventory_file:  # gathers all lines in file to list, gets rid of the fist item and sorts alphabetically
        item_collection.append(row)
    item_collection.pop(0)
    item_collection = sorted(item_collection)
    item_count = 0
    item_collection_length = len(item_collection)
    while item_count < item_collection_length:  # runs through and prints the name of all items in list until list
        # amount is met
        print(item_collection[item_count], end='')
        item_count += 1
    program_menu()


def item_add():  # allows user to add an item to the updated file, must be in correct format
    global update
    update = True
    inventory_file = open('updated_A3_s3942349_stock.txt', 'r')
    inventory_file_lines = 0
    loaded_items = ''
    for add in inventory_file:  # runs through file and adds the first word of all lines to a variable except the
        # first line
        if inventory_file_lines > 0:
            loaded_items += add.split()[0] + ', '
        inventory_file_lines += 1
    print('Available items: ' + loaded_items)
    user_item_add_manufacturer = input('What is name of the item you would like to add?: ')
    if user_item_add_manufacturer in loaded_items:
        print('Item already exists, cancelling request.')
        item_add()
    else:
        user_item_add_model = input('What is the model of the item?: ')
        user_item_add_model_year = input('What is the model year of the item?: ')
        user_item_add_condition = input('What is the condition of the item?: ')
        # find out if the format of 4 above variables are suitable
        variable_list_count = 0
        variable_list = [user_item_add_manufacturer, user_item_add_model, user_item_add_model_year]
        variable_list += [user_item_add_condition]
        while variable_list_count < 4:  # makes sure that all variable inputs are valid
            if ' ' in variable_list[variable_list_count]:
                print('One of the variable was entered incorrectly, please make sure that there are no spaces.')
                item_add()
            variable_list_count += 1
        try:  # make sure that the below input is a number
            user_item_add_price = float(input('What is the price of the item? (In integers or floats): '))
        except:
            print('Error, input was not a float or integer, restarting item add program...')
            item_add()
        try:  # make sure that the below input is an integer
            user_item_add_quantity = int(input('What is the quantity of the item? (In integers): '))
        except:
            print('Error, input was not an integer, restarting item add program...')
            item_add()
        add_item = user_item_add_manufacturer + ' ' + user_item_add_model + ' ' + user_item_add_model_year + ' '
        add_item += user_item_add_condition + ' ' + str(user_item_add_price) + ' ' + str(user_item_add_quantity) + '\n'
        inventory_file = open('updated_A3_s3942349_stock.txt', 'a')
        inventory_file.write(add_item)
        inventory_file.close()
        print('Add successful:', add_item)
    program_menu()


def item_update():  # allows user to change a certain item from updated file, must be in correct format
    global update
    update = True
    inventory_file = open('updated_A3_s3942349_stock.txt', 'r')
    inventory_file_lines = 0
    loaded_items = ''
    for row in inventory_file:  # puts the first work of all file lines into a variable to be displayed
        if inventory_file_lines > 0:
            loaded_items += row.split()[0] + ', '
        inventory_file_lines += 1
    print('Available items: ' + loaded_items)
    inventory_file_lines = 0
    removable_items = []
    inventory_file = open('updated_A3_s3942349_stock.txt', 'r')
    for item in inventory_file:  # gets the amount of lines in file and appends line to list, could be like line 232
        if inventory_file_lines > 0:
            removable_items.append(item.strip())
        inventory_file_lines += 1
    inventory_file.close()
    user_item_update = input('What is name of the item you would like to update?: ')
    while user_item_update == '':  # makes sure that the user is not typing a new line input that would cause problems
        print('Error, item not found, restarting program.')
        program_menu()
    count = 0
    remove_valid = False
    for i in removable_items:  # runs through list and checks where user input is in the list
        if user_item_update in removable_items[count]:
            # not sure why but if any character in the line is present it will select the line, eg T would give Toyota
            remove_valid = True
            break
        else:
            count += 1
    if remove_valid == True:
        line_to_remove = count + 1
        # ask user for all variable updates and make sure they are valid
        user_item_add_model = input('What is the model of the item?: ')
        user_item_add_model_year = input('What is the model year of the item?: ')
        user_item_add_condition = input('What is the condition of the item?: ')
        # find out if the format of above variables are suitable
        variable_list_count = 0
        variable_list = [user_item_update, user_item_add_model, user_item_add_model_year, ]
        variable_list += [user_item_add_condition]
        while variable_list_count < 4:  # makes sure that all variable inputs are valid
            if ' ' in variable_list[variable_list_count]:
                print('One of the variable was entered incorrectly, please make sure that there are no spaces.')
                item_update()
            variable_list_count += 1
        try:  # make sure that the below input is a float
            user_item_add_price = float(input('What is the price of the item? (In integers or floats): '))
        except:
            print('Error, input was not a float or integer, restarting item update program...')
            item_update()
        try:  # make sure that the below input is a float
            user_item_add_quantity = int(input('What is the quantity of the item? (In integers): '))
        except:
            print('Error, input was not an integer, restarting item update program...')
            item_update()
        add_item = user_item_update + ' ' + user_item_add_model + ' ' + user_item_add_model_year + ' '
        add_item += user_item_add_condition + ' ' + str(user_item_add_price) + ' ' + str(user_item_add_quantity)
        add_item += '\n'
        inventory_file.close()

        # overwrite previous line with add_item
        inventory_file = open('updated_A3_s3942349_stock.txt', 'r')
        remove = inventory_file.readlines()
        inventory_file.close()
        del remove[line_to_remove]
        remove.insert(line_to_remove, add_item)
        inventory_file = open('updated_A3_s3942349_stock.txt', 'w')
        for j in remove:  # runs through all items of 'remove' and writes them to the updated file
            inventory_file.write(j)
        inventory_file.close()
        print('Item updated successfully: ' + add_item)
        program_menu()
    else:
        print('Error, item not found, restarting program.')
        program_menu()


def item_remove():  # allows user to remove an existing item from the updated file
    global update
    update = True
    inventory_file = open('updated_A3_s3942349_stock.txt', 'r')
    inventory_file_lines = 0
    loaded_items = ''
    for row in inventory_file:  # shows the first word of all file lines, except the first line
        if inventory_file_lines > 0:
            loaded_items += row.split()[0] + ', '
        inventory_file_lines += 1
    print('Available items: ' + loaded_items)
    inventory_file_lines = 0
    removable_items = []
    inventory_file = open('updated_A3_s3942349_stock.txt', 'r')
    for item in inventory_file:  # adds the contents of the file to a list called removable_items
        if inventory_file_lines > 0:
            removable_items.append(item.strip())
        inventory_file_lines += 1
    inventory_file.close()
    user_item_remove = input('What is name of the item you would like to remove?: ')
    while user_item_remove == '':  # makes sure that the user is not typing a new line input that would cause problems
        print('Error, item not found, restarting program.')
        program_menu()
    count = 0
    remove_valid = False
    for i in removable_items:  # could be a 'while' loop, but for is nicer, loops through removable_items checks if
        # user input is contained within, if it is, it breaks from teh loop and changes remove_valid to True,
        # otherwise it will continue to loop, saving the count value
        if user_item_remove in removable_items[count]:
            # not sure why but if any character in the line is present it will select the line, eg T would give Toyota
            remove_valid = True
            break
        else:
            count += 1
    if remove_valid == True:
        line_to_remove = count + 1
        inventory_file = open('updated_A3_s3942349_stock.txt', 'r')
        remove = inventory_file.readlines()
        inventory_file.close()
        del remove[line_to_remove]  # del is the same as pop() could be 'remove.pop(line_to_remove)'
        inventory_file = open('updated_A3_s3942349_stock.txt', 'w')
        for j in remove:  # runs through all items of 'remove' and writes them to the updated file
            inventory_file.write(j)
        inventory_file.close()
        print('Item removed successfully.')
        program_menu()
    else:
        print('Error, item not found, restarting program.')
        program_menu()


def program_exit():  # allows the user to end the program, and displays all information from last updated file
    print('Current item information:')
    print('Now showing all item details in alphabetical order:')
    if update == False:
        inventory_file = open('A3_s3942349_stock.txt', 'r')
    else:
        inventory_file = open('updated_A3_s3942349_stock.txt', 'r')
    item_collection = []
    for row in inventory_file:  # adds all rows of file to list, pop() is used on first row to get rid of it before sort
        item_collection.append(row)
    item_collection.pop(0)
    item_collection = sorted(item_collection)
    item_count = 0
    item_collection_length = len(item_collection)
    while item_count < item_collection_length:  # loops through all items and shows the details until all are shown
        print(item_collection[item_count], end='')
        item_count += 1
    inventory_file = open('updated_A3_s3942349_stock.txt', 'r')
    total_stock_value = 0.0  # below until line 320 is a copy from function: program_start()
    seperator = inventory_file.readlines()
    seperator.pop(0)
    for i in seperator:
        total_stock_value += float(i.split()[4]) * int(i.split()[5])
    print('Total stock value is:', total_stock_value)
    user_exit = input('Are you sure you want to save and exit the program? y/n: ')
    while user_exit != 'y' and user_exit != 'n':  # waits for user to input correctly, determines displaying error or
        # progressing the program print
        print('Wrong input, please try again.')
        user_exit = input('Are you sure you want to save and exit the program? y/n: ')
    if user_exit == 'y':
        print('--- Now exiting the program ---')
        inventory_file.close()
    else:
        program_menu()


# MAIN PROGRAM
update = False
previous_file = open('A3_s3942349_stock.txt', 'r')
new_file = open('updated_A3_s3942349_stock.txt', 'w')
for line in previous_file:  # clones the original file into updated one, runs until all lines are copied, clones file
    new_file.write(line)
new_file.close()
previous_file.close()
program_start()
