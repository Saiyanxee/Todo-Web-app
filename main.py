import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state['add_todo']+"\n"
    todos.append(todo)
    functions.writing_todos(todos)


st.header("My TO-DO APP")
st.subheader("Created by Saiyanxee")
st.text("This app is created to increase your productivity")
for index, todo in enumerate(todos):
    checkbox=st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.writing_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Enter todo",
              on_change=add_todo, key='add_todo')
