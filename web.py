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

for index, todo in enumerate(session_state.todos):
    check_box = checkbox(todo, key=todo)
    if check_box:
       session_state.todos.pop(index)
       functions.write_todos(session_state.todos)
       del session_state[todo]
       experimental_rerun()




