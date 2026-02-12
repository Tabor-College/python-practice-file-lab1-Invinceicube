import sys # Assists exit on command "13"
task_list = []

while True: # Asking until the user enters a valid integer for the loop
    try: # Avoids non-integer error
        task_amount = int(input("Hello student! Please enter the amount of commands you will use on your task tracking list! : " )) # User input for how many commands will run inside the 'MAIN' for loop
        if task_amount < 0:
            print("Please enter a positive number.")
        else:
            break
    except ValueError: # Avoids non-integer error
        print("Invalid input. Please enter a number.")

for i in range(task_amount): # This is the 'MAIN' for loop... (looping by declared input value)
    while True:  # Loops until a valid command is entered
        print(
        """\nList Menu:
        
        1. Add a new option = "Add"
        2. Insert a task at a position = "Insert"
        3. Remove a task by name = "Remove By Name"
        4. Remove a task by index = "Remove By Index"
        5. Update a task = "Update" 
        6. View all tasks= "View"
        7. Sort tasks = "Sort"
        8. Reverse tasks = "Reverse"
        9. Search for a task = "Search"
        10. Task statistics = "Stats"
        11. Copy task list = "Copy"
        12. Clear all tasks = "Clear"
        13. Exit = "Exit" """)
    
        command = input(f"\nEnter command {i+1}: ")
        if command.lower() == "add" or command == "1":
            while True:
                new_task = input("input your task to add to the list: ")
                if new_task == "":
                    print("Error, please enter a task that is not blank...")
                else:
                    task_list.append(new_task)
                    print(task_list)
                    break
            break

        elif command.lower() == "insert" or command == "2": # ".lower" avoids the requirement for capital letter inputs
            success = False
            while True:
                try: # Avoids non-integer error
                    position_index = int(input("enter the position in the list: ")) # Asks user to input index number
                    if 0 <= position_index < len(task_list):
                        new_task = input("input your task to add to the list: ")
                        task_list.insert(position_index, new_task)
                        print(task_list)
                        success = True
                        break
                    else:
                        print("ERROR, Please enter a valid index number")
                except ValueError: # Avoids non-integer error
                    print("Please enter a number...")
            if success:
                break

        elif command.lower() == "remove by name" or command == "3":
            success = False # Forcing the code to only move onto next command if the command succeeds

            while True:
                if len(task_list) == 0: # Returns to the "enter command" if the list is empty
                    print("Your task list is empty!")
                    break
                else:
                    deleted_task = input("input the task name to remove from the list: ")
                    if  deleted_task in task_list:
                        task_list.remove(deleted_task)
                        print("task Removed Successfully")
                        print(task_list)
                        success = True
                        break
                    else:
                        print(f"ERROR: Task '{deleted_task}' is not in the list.")
            if success:
                break
        
        elif command.lower() == "remove by index"  or command == "4":
            success = False # Forcing the code to only move onto next command if the command succeeds

            while True:
                    if len(task_list) == 0: # Returns to the "enter command" if the list is empty
                        print("Your task list is empty!")
                        break # Return to command menu (soft-lock prevention)

                    escape_or_index_input = input("enter the index number of the task or enter 'c' to cancel the command: ")
                    
                    if escape_or_index_input.lower() == "c": # Forced item removal prevention (assuming user accidentally pressed "4")
                        print("Escaping to main menu...")
                        break # Return to main menu
                    try: # Avoids non-integer error
                        deleted_index = int(escape_or_index_input) # converting entered index number to integer

                        if 0 <= deleted_index < len(task_list):
                            task_list.pop(deleted_index)
                            print("task Removed Successfully")
                            print(task_list)

                            success = True
                            break               

                        else:
                            print(f"ERROR: Task position '{deleted_index}' is not in the list.")
                    except ValueError: # Avoids non-integer error
                        print("ERROR: Invalid input. Please enter a whole number.")
            if success: # Forces successful use of index removal in order to move to the next command
                break # Exits command menu loop
        
        elif command.lower() == "update" or command == "5":
            success = False # Forcing the code to only move onto next command if the command succeeds
            while True:
                if len(task_list) == 0: # Returns to the "enter command" if the list is empty
                    print("Your list is empty!")
                    break
                else:
                    try: # Avoids non-integer error
                        while True:

                            update_position_index = int(input("enter the position in the list: ")) # Asks user to input index number
                            if 0 <= update_position_index < len(task_list):
                                updated_task = input("input your updated task to add to the list: ")
                                task_list[update_position_index] = updated_task
                                print(task_list)
                                success = True                
                                break
                            else:
                                print("ERROR: Index number not in the list. Please enter a valid index number...")
                        break
                    except ValueError: # Avoids non-integer error
                        print("Invalid input! Please enter a number...")

            if success:
                break
        
        elif command.lower() == "view" or command == "6" or command.lower() == "veiw":
            if len(task_list) == 0: # Returns to the "enter command" if the list is empty
                print("Your list is empty!")
            else:
                print("Current tasks with indexes:")
                for index, task in enumerate(task_list):
                    print(f"{index}: {task}")
            break
        
        elif command.lower() == "sort" or command == "7":
            if len(task_list)  < 2: # Returns to the "enter command" if the list is empty
                print("Your list is too small to sort!")
            else:
                task_list.sort()
                print(task_list)
                break

        elif command.lower() == "reverse" or command == "8":
            if len(task_list) == 0: # Returns to the "enter command" if the list is empty
                print("Your list is currently empty")
            else:
                task_list.reverse()
                print(task_list)
                break
        
        elif command.lower() == "search" or command == "9":
            if len(task_list) == 0: # Returns to the "enter command" if the list is empty
                print("Your list is currently empty")
            
            else:
                search_success = False # Allows only sucessful searches to advance the 'MAIN' for loop
                while True:
                    print("""\nHere are the available search methods!
                          
                        1. Name (1)
                        2. Count (2)
                        3. Index (3)
                        4. Exit (4) """) # Splitting the search command into three subsets
                    search_method = input("\nplease choose a search method: ")
                    if search_method.lower() == "name" or search_method == "1" or search_method == "(1)":
                        task_name = input("Enter the task name to search for: ")
                        if task_name in task_list:
                            print(f"'{task_name}' is in your task list.")
                            search_success = True
                            break
                        else:
                            print(f"SEARCH ERROR: '{task_name}' is NOT in your task list.")
                            search_success = True
                            break

                    elif search_method.lower() == "count" or search_method == "2" or search_method == "(2)":
                        task_name = input("\nEnter the task name to search for: ")
                        print(f"{task_name} appears {task_list.count(task_name)} times in your task list.")
                        search_success = True
                        break
                    
                    elif search_method.lower() == "index" or search_method == "3" or search_method == "(3)":
                      
                            success = False

                            while not success:
                                try:

                                    task_index_no = int(input("\nPlease input the index number of your task to find its index number: ")) # Asks user to input index number
                                    print
                                    if 0 <= task_index_no < len(task_list):
                                            print(f"index number '{task_index_no}' is currently '{task_list[task_index_no]}'!") # Searches VIA index number
                                            success = True
                                            search_success = True
                                            break
                                    else: 
                                            print(f"SEARCH ERROR: Index number '{task_index_no}' is NOT in your task list. (Index number is out of range)")
                                except ValueError:
                                    print("\nPlease enter an integer...")
                            if success:
                                break
                    elif search_method.lower() == "exit" or search_method == "4" or search_method  == "(4)":
                        break
                    
                    else:
                        print("\nplease enter one of the four valid commands!")

            if search_success == True:
                break


        elif command.lower() == "stats" or command == "10":
            success = False
            while True: 

                if len(task_list) == 0: # Returns to the "enter command" if the list is empty
                    print("Your list is currently empty")
                else:
                    total = len(task_list)
                    first_task = task_list[0]
                    last_task = task_list[-1]
                    print("Task Statistics:")
                    print(f"• Total number of tasks: {total}")
                    print(f"• First task: {first_task}")
                    print(f"• Last task: {last_task}")
                    success = True
                break
            if success: 
                break

        elif command.lower() == "copy" or command == "11":
            if len(task_list) == 0: # Returns to the "enter command" if the list is empty
                print("ERROR: Your task list is empty")
            
            else:
                task_list_copy = task_list.copy()
                print(f"Original: {task_list}, Copy: {task_list_copy}")
            break

        elif command.lower() == "clear" or command == "12":
            if len(task_list) == 0: # Returns to the "enter command" if the list is empty
                print("Your task list is already empty!")
            else:
                task_list.clear()
                print("Your task list has been cleared successfully!")
                print(task_list)
            break
        elif command.lower() == "exit" or command == "13":
            print("Thank you for playing!")
            sys.exit() # Exits the entire codee

        else:
            print("Please enter a valid command!")
# Reflection 

""" 1: Pop() Would remove a task by it's given index/osition in the list, 
    Remove() would remove the value by name/value

    2: copy() creates an entire new list that is a clone of the first
       Assignment(=) means list 1 = list 2, 
       meaning they cannot be edited independently
       as they are not seperate lists.
       
       To modify a cloned list, it is safer to copy 
       as it will perserve the original list

    3: sort() orders the list in (numerical order for integers)
        & (alphabetical order for strings),
        you can also add custom keys/specifacations

    4: List indexing allows you update, add, remove, etc... elements by their position.
       Indexing begins with the frist variable in the list being equal to 0
       the list then counts upwards, depeding on where a variable is in the list
       will determine its index value. 
       Negative indices count backwards from the end of the list.
       You can also slice the or make ranges between variables using index values
     """

# Good soup
