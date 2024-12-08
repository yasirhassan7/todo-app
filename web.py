import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my Task List")
st.write("This app helps me track my task list")


st.text_input(label="Enter your Task List:", placeholder="Enter item...")
for todo in todos:
    st.checkbox(todo)