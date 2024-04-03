from functions import get_todos, write_todos
import time


now = time.strftime("%B %d, %Y %I:%M:%S %p")
print("Today's date:", now)


while True:
    user_select = input("Select Add, Show, Edit, Complete, Exit: ")
    user_select = user_select.title()

    if user_select.startswith("Add"):
        todo = user_select[4:]

        todos = get_todos()

        todos.append(todo.title() + "\n")

        write_todos(todos)
    elif user_select.startswith('Show') or user_select.startswith('Display'):
        todos = get_todos()

        # ********** LONG METHOD **********
        # new_todos = []
        # for todo in todos:
        #     new_todos.append(todo.strip("\n"))

        # ********** SHORT METHOD USING LIST COMPREHENSION **********
        new_todos = [todo.strip('\n') for todo in todos]

        if len(new_todos) > 0:
            for i, item in enumerate(new_todos):
                print(f"{i+1}-{item}")
        else:
            print("No todos found. Please add new todos")
    elif user_select.startswith('Edit'):
        try:
            todos = get_todos()

            number = int(user_select[5:])
            item_change = input("Change item to: ").title()

            if number > len(todos):
                print("Invalid item number. Not exist!")
            else:
                number = number - 1
                todos[number] = item_change + "\n"

                write_todos(todos)
        except ValueError:
            print("Invalid command there are no such number")
            continue
    elif user_select.startswith('Complete'):
        try:
            todos = get_todos()

            new_todos = [item.strip('\n') for item in todos]

            for i, item in enumerate(new_todos):
                print(f"{i+1}-{item}")

            number = int(user_select[9:])
            remove_item = todos.pop(number-1)

            write_todos(todos)

            print(f"Todos *{remove_item}* has been completed")
        except IndexError:
            print("Invalid value. There is no such value")
            continue
    elif user_select.startswith('Exit'):
        break
    else:
        print("Hey, you entered an unknown command")

print("Thank you and Bye!")
