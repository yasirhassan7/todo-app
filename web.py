from streamlit import subheader, text_input, checkbox, session_state, title, write
import functions

if "todos" not in session_state:
    session_state.todos = functions.get_todos()
#todos = functions.get_todos()

def add_todo():
    new_todo = session_state["new_todo"]
    if new_todo:
        session_state.todos.append(new_todo)
        functions.write_todos(session_state.todos)
        session_state["new_todo"] = ""
    #todos.append
    #functions.write_todos(todos)

title("My Todo App")
subheader("This is my Task List")
write("This app helps me track my task list")

text_input(label="Enter your Task List:",
           placeholder="Enter item...",
           on_change=add_todo, key='new_todo')

for todo in session_state.todos:
    checkbox(todo)




