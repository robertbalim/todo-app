# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%A %m/%d/%Y %I:%M:%S %p")
print("It is", now)

while True:
    user_input = input("Type Add, Show, Edit, Complete or Exit: ")
    user_input = user_input.strip().capitalize()

    if user_input.startswith("Add") or user_input.startswith("New"):
        todos = functions.get_todos()

        todo = user_input[4:]
        todos.append(todo.capitalize() + "\n")

        functions.write_todos(todos)

    elif user_input.startswith("Edit"):
        try:
            todos = functions.get_todos()

            # for index, todo in enumerate(todos):
            #     print(f"{index + 1}--{todo}", end="")

            edit_item = int(user_input[5:])
            change_item = input("Enter the todo replacement: ")
            todos[edit_item - 1] = change_item.capitalize() + "\n"

            functions.write_todos(todos)

            print("Item change successfully!")
        except ValueError:
            print("Your command is not valid")
    elif user_input.startswith("Show"):
        todos = functions.get_todos()

        if len(todos) <= 0:
            print("There is no record to show!")
        else:
            for index, todo in enumerate(todos):
                print(f"{index + 1}--{todo}", end="")
    elif user_input.startswith("Complete"):
        try:
            todos = functions.get_todos()

            done_todo = int(user_input[9:])
            done_todo = todos.pop(done_todo - 1)

            functions.write_todos(todos)

            print("Todo has been completed!", done_todo)
        except IndexError:
            print("There is no number with that item")
    elif user_input.startswith("Clear"):
        if input("Are you sure to delete all records?").capitalize() == "Yes":
            file = open('todos.txt', 'w')
            file.close()
        print("All records has been deleted!")
    elif user_input.startswith("Exit"):
        break
    else:
        print("Invalid command!")

print("Bye!")
