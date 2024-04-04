import PySimpleGUI as Psg
from functions import get_todos, write_todos

Psg.theme("DarkBlue3")
Psg.set_options(font=("Gill Sans MT", 12))

todos = get_todos()

label = Psg.Text("Type in your todos")
input_box = Psg.InputText(size=(50, 40), tooltip="Enter todo here", key="-INPUT-")
button_close = Psg.Button("Exit", enable_events=True)
button_add = Psg.Button("Add", enable_events=True, size=(None, 1))
button_edit = Psg.Button("Edit", enable_events=True, size=(None, 1))
button_remove = Psg.Button("Remove", enable_events=True, size=(None, 1))
listbox_todo = Psg.Listbox(todos, size=(50, 10), enable_events=True, no_scrollbar=True, key="-LIST_TODO-")

window = Psg.Window("My To-Do App", size=(650, 400), icon="icon/todo.ico", enable_close_attempted_event=True,
                    layout=[[label],
                            [input_box, button_add],
                            [listbox_todo, button_edit, button_remove],
                            [button_close]])

while True:
    event, values = window.read()

    if event == "Add":
        todo = values["-INPUT-"].strip() + "\n"
        todos.append(todo)
        window["-LIST_TODO-"].update(todos)
        window["-INPUT-"].update("")

        write_todos(todos)
    elif event == "Edit":
        todo_to_edit = values["-LIST_TODO-"][0]
        new_todo = values['-INPUT-'].strip() + "\n"

        index = todos.index(todo_to_edit)
        todos[index] = new_todo
        window["-LIST_TODO-"].update(todos)
        window["-INPUT-"].update("")

        write_todos(todos)
    elif event == "Remove":
        index = listbox_todo.get_indexes()[0]
        todos.pop(index)
        window["-LIST_TODO-"].update(todos)

        write_todos(todos)
    elif event == "-LIST_TODO-":
        todo_selected = values["-LIST_TODO-"][0].strip()
        window["-INPUT-"].update(todo_selected)
    elif event == Psg.WINDOW_CLOSE_ATTEMPTED_EVENT:
        break
    elif event == Psg.WIN_CLOSED or event == "Exit":
        break

window.close()
