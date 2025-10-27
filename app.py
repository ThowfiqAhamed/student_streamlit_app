import streamlit as st
import mysql.connector
import pandas as pd

# ==========================
# Database Connection Setup
# ==========================
def get_connection():
    return mysql.connector.connect(
        host="di2txn.h.filess.io",
        user="student_details_spiritpen",
        password="f8cf91dfaffca17be403d133d42b88c4893ff1fc",
        database="student_details_spiritpen",
        port=3307
    )

st.set_page_config(page_title="Student Database", page_icon="🎓", layout="centered")
st.title("🎓 Student Management System")
st.markdown("This app is connected to your **Filess.io MySQL Database** ✅")

# ==========================
# Helper Functions
# ==========================
def insert_student(name, age):
    db = get_connection()
    cursor = db.cursor()
    sql = "INSERT INTO st_datas (name, age) VALUES (%s, %s)"
    cursor.execute(sql, (name, age))
    db.commit()
    db.close()

def view_students():
    db = get_connection()
    df = pd.read_sql("SELECT * FROM st_datas", db)
    db.close()
    return df

def update_student(name, new_age):
    db = get_connection()
    cursor = db.cursor()
    sql = "UPDATE st_datas SET age = %s WHERE name = %s"
    cursor.execute(sql, (new_age, name))
    db.commit()
    db.close()

def delete_student(name):
    db = get_connection()
    cursor = db.cursor()
    sql = "DELETE FROM st_datas WHERE name = %s"
    cursor.execute(sql, (name,))
    db.commit()
    db.close()

# ==========================
# Sidebar Navigation
# ==========================
menu = ["Add Student", "View Students", "Update Student", "Delete Student"]
choice = st.sidebar.radio("Select Option", menu)

# ==========================
# 1️⃣ Add Student
# ==========================
if choice == "Add Student":
    st.subheader("➕ Add New Student")
    name = st.text_input("Enter Student Name")
    age = st.number_input("Enter Age", min_value=1, max_value=100, step=1)
    if st.button("Add Student"):
        if name.strip() == "":
            st.warning("⚠️ Please enter a valid name")
        else:
            insert_student(name, age)
            st.success(f"✅ Added student '{name}' (Age {age}) successfully!")

# ==========================
# 2️⃣ View Students
# ==========================
elif choice == "View Students":
    st.subheader("📋 View All Students")
    df = view_students()

    if df.empty:
        st.warning("No student records found.")
    else:
        search = st.text_input("🔍 Search by name")
        if search:
            df = df[df['name'].str.contains(search, case=False)]
        st.dataframe(df, use_container_width=True)

# ==========================
# 3️⃣ Update Student
# ==========================
elif choice == "Update Student":
    st.subheader("🔄 Update Student Age")
    df = view_students()

    if df.empty:
        st.warning("No records available to update.")
    else:
        names = df['name'].tolist()
        selected_name = st.selectbox("Select Student", names)
        new_age = st.number_input("Enter New Age", min_value=1, max_value=100, step=1)
        if st.button("Update Age"):
            update_student(selected_name, new_age)
            st.success(f"✅ Updated '{selected_name}' age to {new_age}!")

# ==========================
# 4️⃣ Delete Student
# ==========================
elif choice == "Delete Student":
    st.subheader("🗑️ Delete Student Record")
    df = view_students()

    if df.empty:
        st.warning("No records available to delete.")
    else:
        names = df['name'].tolist()
        selected_name = st.selectbox("Select Student to Delete", names)
        if st.button("Delete"):
            delete_student(selected_name)
            st.success(f"🗑️ Deleted record for '{selected_name}' successfully!")


