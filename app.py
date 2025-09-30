import streamlit as st
import os


def main():
    st.title("Your Secret-Powered To-Do List")

    # Get secrets from environment (to demo secrets injection)
    user_name = os.getenv("USER_NAME", "Guest User")
    api_token = os.getenv("API_TOKEN", None)

    st.write(f"Hello, **{user_name}**! Welcome to your to-do list.")

    if api_token:
        st.write(f"Your API token is: `{api_token[:4]}****` (kept secret!)")

    # Initialize session state for to-dos
    if "todos" not in st.session_state:
        st.session_state["todos"] = []

    todo_input = st.text_input("Add a new to-do item:")

    if st.button("Add"):
        if todo_input:
            st.session_state.todos.append(todo_input)
            st.experimental_rerun()

    # Display to-do items with delete buttons
    for idx, todo in enumerate(st.session_state.todos):
        col1, col2 = st.columns([0.9, 0.1])
        col1.write(todo)
        if col2.button("❌", key=idx):
            st.session_state.todos.pop(idx)
            st.experimental_rerun()


if __name__ == "__main__":
    main()
