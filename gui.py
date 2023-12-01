from functions import get_todos, write_todos
import PySimpleGUI as Psg

label = Psg.Text("Type in a todo")
input_text = Psg.InputText(tooltip="Enter todo here", key="todo")
button = Psg.Button("Add")

window = Psg.Window("My To-Do App",
                    layout=[[label], [input_text, button]],
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

        case Psg.WIN_CLOSED:
            break


window.close()
