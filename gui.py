import functions
import PySimpleGUI as Psg

label = Psg.Text("Type in a todo")
input_text = Psg.InputText(tooltip="Enter todo here")
button = Psg.Button("Add")

window = Psg.Window("My To-Do App", layout=[[label], [input_text, button]])
window.read()
print("Hello")
window.close()
