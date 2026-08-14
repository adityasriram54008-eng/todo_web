import streamlit as st
import functions

st.set_page_config(layout='wide')
todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo']+'\n'
    todos.append(todo)
    functions.write_todos(todos)

st.title('My Todos App')
#could use st.subheader or st.write as other ways to display text,
#can bold the st.write('<b>....<b>', unsafe_allow_html = True)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key = todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label = 'Enter a TODO', placeholder = 'Add new TODO...', on_change = add_todo, key = 'new_todo')