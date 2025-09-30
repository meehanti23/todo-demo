import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def main():
    st.title("Your To-Do List")

    # Get demo secrets from environment
    user_name = os.getenv("USER_NAME", "Guest User")
    api_token = os.getenv("API_TOKEN", None)

    st.write(f"Hello, **{user_name}**! Welcome to your to-do list.")

    # Initialize session state for to-dos
    if "todos" not in st.session_state:
        st.session_state["todos"] = []

    def add_todo():
        if st.session_state.todo_input:
            st.session_state.todos.append(st.session_state.todo_input)
            st.session_state.todo_input = ""

    todo_input = st.text_input(
        "Enter a to-do item:", key="todo_input", on_change=add_todo
    )

    # Display to-do items with delete buttons
    for idx, todo in enumerate(st.session_state.todos):
        col1, col2 = st.columns([0.9, 0.1])
        col1.write(todo)
        if col2.button("❌", key=idx):
            st.session_state.todos.pop(idx)
            st.rerun()


if __name__ == "__main__":
    main()
