from functions import get_todos, write_todos
import PySimpleGUI as Psg
import time

# Psg.theme_previewer()
Psg.theme("BluePurple")
clock = Psg.Text("", key="clock")
label = Psg.Text("Type in a todo")
input_text = Psg.InputText(tooltip="Enter todo here", key="todo")
button = Psg.Button("Add", key="Add")

listbox = Psg.Listbox(values=get_todos(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = Psg.Button("Edit", key="Edit")
complete_button = Psg.Button("Complete")
close_button = Psg.Button("Close")

window = Psg.Window("My To-Do App",
                    layout=[[clock], [label],
                            [input_text, button],
                            [listbox, edit_button, complete_button],
                            [close_button]],
                    font=("Helvetica", 20))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%A %m/%d/%Y %I:%M:%S %p"))
    match event:
        case "Add":
            if values["todo"] == "":
                Psg.popup("Please enter the todo first", font=("Helvetica", 20))
            else:
                todos = get_todos()
                new_todo = values["todo"] + "\n"
                todos.append(new_todo)
                write_todos(todos)
                window["todos"].update(values=todos)
                input_text.Update(value="")
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]

                todos = get_todos()
                i = todos.index(todo_to_edit)
                todos[i] = new_todo + "\n"

                write_todos(todos)
                window["todos"].update(values=todos)
                input_text.Update(value="")
            except IndexError:
                Psg.popup("Please select the todo to edit", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = get_todos()
                todos.remove(todo_to_complete)
                write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                Psg.popup("Please select the todo to complete", font=("Helvetica", 20))
        case "todos":
            window["todo"].update(value=values['todos'][0])
        case "Close":
            break
        case Psg.WIN_CLOSED:
            break


window.close()
