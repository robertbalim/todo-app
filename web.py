import streamlit as st
from functions import get_todos, write_todos

st.title("My Todo app")
st.subheader("This is my todo list")
st.write("This app is to increase your productivity.")

todos = get_todos()

for todo in todos:
    st.checkbox(todo)

st.text_input("Enter todos here", help="Enter todos here", placeholder="Add new todo...", key="todo")
