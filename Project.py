# import mysql.connector
#
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root",
#     database="mkb_project",
#     port="3306"
# )
# cursor = db.cursor()
#
# def insert_student():
#     s_no = int(input("Enter S_no: "))
#     name = input("Enter Student Name: ")
#     reg_no = input("Enter Reg_no: ")
#     dept = input("Enter Department: ")
#     tamil = int(input("Enter Tamil Marks: "))
#     english = int(input("Enter English Marks: "))
#     maths = int(input("Enter Maths Marks: "))
#     science = int(input("Enter Science Marks: "))
#     social = int(input("Enter Social Marks: "))
#
#     sql = """
#     INSERT INTO project (s_no, name, reg_no, dept, tam, eng, mat, sci, soc)
#     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
#     """
#     values = (s_no, name, reg_no, dept, tamil, english, maths, science, social)
#     cursor.execute(sql, values)
#     db.commit()
#     print(" Student added successfully!\n")
#
#
# def view_students():
#     cursor.execute("SELECT * FROM project")
#     rows = cursor.fetchall()
#     for x in rows :
#         print(x)
#     # if rows:
#     #     print("\n STUDENT RECORDS:")
#     #     print("-" * 100)
#     #     for row in rows:
#     #         print(f"S_no: {row[0]} | Name: {row[1]} | Reg_no: {row[2]} | Dept: {row[3]} | "
#     #               f"Tamil: {row[4]} | English: {row[5]} | Maths: {row[6]} | Science: {row[7]} | Social: {row[8]}")
#     #     print("-" * 100)
#     # else:
#     #     print("\n No student records found!\n")
# #
# def update_student():
#     s_no = input("Enter S_no of student to update: ")
#
#     print("Which subject do you want to update?")
#     print("1. Tamil\n2. English\n3. Maths\n4. Science\n5. Social")
#     choice = int(input("Enter choice: "))
#
#     subjects = {1: "tamil", 2: "english", 3: "maths", 4: "science", 5: "social"}
#     if choice in subjects:
#         subject_name = subjects[choice]
#         new_mark = int(input(f"Enter new mark for {subject_name.capitalize()}: "))
#
#         sql = f"UPDATE project SET {subject_name} = %s WHERE s_no = %s"
#         cursor.execute(sql, (new_mark, s_no))
#         db.commit()
#         print(" Marks updated successfully!\n")
#     else:
#         print(" Invalid choice!\n")
#
# def delete_student():
#     s_no = input("Enter S_no of student to delete: ")
#     sql = "DELETE FROM project WHERE s_no = %s"
#     cursor.execute(sql, (s_no,))
#     db.commit()
#     print("Student deleted successfully!\n")
#
# def main():
#     while True:
#         print("\n=== STUDENT MARKS REGISTRATION SYSTEM ===")
#         print("1. Insert Student")
#         print("2. View Students")
#         print("3. Update Student Marks")
#         print("4. Delete Student")
#         print("5. Exit")
#
#         choice = int(input("Enter your choice: "))
#
#         if choice == 1:
#             insert_student()
#         elif choice == 2:
#             view_students()
#         elif choice == 3:
#             update_student()
#         elif choice == 4:
#             delete_student()
#         elif choice == 5:
#             print(" Exiting...")
#             break
#         else:
#             print("Invalid choice! Please try again.\n")
#
# main()
#
# cursor.close()
# db.close()

import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(
    host="di2txn.h.filess.io",
    user="student_details_spiritpen",        # change if needed
    password="f8cf91dfaffca17be403d133d42b88c4893ff1fc",        # enter your MySQL password
    database="student_details_spiritpen",   # make sure this DB exists
    port=3307
)

mycursor = mydb.cursor()
def insert_data():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    sql = "INSERT INTO st_datas (name, age) VALUES (%s, %s)"
    mycursor.execute(sql, (name, age))
    mydb.commit()
    print(f"✅ Record added: ({name}, {age})")

def view_data():
    mycursor.execute("SELECT * FROM st_datas ")
    rows = mycursor.fetchall()
    print("\n📋 Current Records:")
    for r in rows:
        print(f"Name: {r[0]}, Age: {r[1]}")

def update_data():
    name = input("Enter name to update: ")
    new_age = int(input("Enter new age: "))
    sql = "UPDATE st_datas  SET age = %s WHERE name = %s"
    mycursor.execute(sql, (new_age, name))
    mydb.commit()
    print(f"🔄 Updated {name}'s age to {new_age}")

def delete_data():
    name = input("Enter name to delete: ")
    sql = "DELETE FROM st_datas WHERE name = %s"
    mycursor.execute(sql, (name,))
    mydb.commit()
    print(f"🗑️ Deleted record for {name}")

while True:
    print("\n===== MENU =====")
    print("1. Insert Data")
    print("2. View Data")
    print("3. Update Data")
    print("4. Delete Data")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        insert_data()
    elif choice == "2":
        view_data()
    elif choice == "3":
        update_data()
    elif choice == "4":
        delete_data()
    elif choice == "5":
        print("👋 Exiting program...")
        break
    else:
        print("❌ Invalid choice, try again!")

# Close connection
mycursor.close()
mydb.close()
