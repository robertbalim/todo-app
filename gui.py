from functions import get_todos, write_todos
import PySimpleGUI as Psg

label = Psg.Text("Type in a todo")
input_text = Psg.InputText(tooltip="Enter todo here", key="todo")
button = Psg.Button("Add", key="Add")
listbox = Psg.Listbox(values=get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = Psg.Button("Edit", key="Edit")

window = Psg.Window("My To-Do App",
                    layout=[[label], [input_text, button], [listbox, edit_button]],
                    font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            write_todos(todos)
            window["todos"].update(values=todos)
            input_text.Update(value="")
        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]

            todos = get_todos()
            i = todos.index(todo_to_edit)
            todos[i] = new_todo + "\n"

            write_todos(todos)
            window["todos"].update(values=todos)
            input_text.Update(value="")
        case "todos":
            window["todo"].update(value=values['todos'][0])
        case Psg.WIN_CLOSED:
            break


window.close()
