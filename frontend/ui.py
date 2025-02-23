import streamlit as st
import requests
import time

# FastAPI server URL
FASTAPI_BASE_URL = "http://backend:8000"

if 'update_triggered' not in st.session_state:
    st.session_state.update_triggered = False

st.title("📋 Welcome to TODO List App 📋")

# Display Current TODOs
with st.expander("📝Current TODOs"):
    response = requests.get(f"{FASTAPI_BASE_URL}/todos")
    if response.status_code == 200:
        todos = response.json()
        if not todos:
            st.markdown("No TODOS!😊")
        else:
            for todo in todos:
                st.markdown(f"* **Task ID:** {todo['id']} **Task:** {todo['task']} **Category:** {todo['category']} **Completed:** {str(todo['completed'])}", unsafe_allow_html=True)
    else:
        st.error("❌Failed to load TODOs")

# Add TODO
with st.form("add_todo", clear_on_submit=True):
    st.subheader("➕Add a New TODO")
    new_task = st.text_input("📝Task")
    new_id = st.number_input("🏷️ID", value=1, format="%d")
    new_category = st.text_input("📂Category")
    submitted = st.form_submit_button("✅Add TODO")
    if submitted:
        todo = {"task": new_task, "id": new_id, "category": new_category, "completed": False}
        response = requests.post(f"{FASTAPI_BASE_URL}/todos", json=todo)
        if response.status_code == 200:
            time.sleep(2)
            st.success("✅TODO added successfully!")
            st.session_state.update_triggered = True
            st.rerun()  # refresh page
        else:
            st.error("❌Failed to add TODO")

# Update/Delete TODO
with st.expander("🔄Update/❌Delete TODO "):
    action = st.radio("Choose action:", options=["Update Task", "Update Completed Status", "Delete TODO"], index=0, key="action")
    task_id = st.number_input("Enter Task ID", value=1, format="%d", key="upd_del")
    task_category = st.text_input("Enter Category", key="category")

    if action == "Update Task":
        updated_task = st.text_input("Update Task", key="task")
        if st.button("Update", key="update_btn"):
            todo = {"task": updated_task, "id": task_id, "category": task_category, "completed": False}
            url = f"{FASTAPI_BASE_URL}/todos/{task_category}/{task_id}"
            response = requests.put(url, json=todo)
            if response.status_code == 200:
                st.success("✅TODO updated successfully!")
                time.sleep(2)
                st.session_state.update_triggered = True
                st.rerun()  # refresh page
            else:
                st.error(f"❌Failed to update TODO. Please check that the task ID and category are correct. Status code: {response.status_code}")
                st.write(response.json())

    elif action == "Update Completed Status":
        new_completed_status = st.checkbox("Completed", key="completed")
        if st.button("Update", key="update_btn"):
            url = f"{FASTAPI_BASE_URL}/todos/complete/{task_category}/{task_id}"
            response = requests.put(url, json={"completed": new_completed_status})
            if response.status_code == 200:
                st.success(f"TODO {task_id} updated!")
                time.sleep(2)
                st.session_state.update_triggered = True
                st.rerun()  # refresh page
            else:
                st.error(f"❌Failed to update TODO. Please check that the task ID and category are correct. Status code: {response.status_code}")
                st.write(response.json())

    elif action == "Delete TODO":
        if st.button("Delete", key="delete_btn"):
            url = f"{FASTAPI_BASE_URL}/todos/{task_category}/{task_id}"
            response = requests.delete(url)
            if response.status_code == 200:
                st.success(f"TODO {task_id} deleted!")
                time.sleep(2)
                st.session_state.update_triggered = True
                st.rerun()  # refresh page
            else:
                st.error(f"❌Failed to delete TODO. Please check the task ID and category. Status code: {response.status_code}")
                st.write(response.json())
