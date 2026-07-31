import os
from add_student import add_student as add_func
from modify_student import modify_student as modify_func
from delete_student import delete_student as delete_func
from view_all_students import view_all_students as view_all_func
from view_student import view_student as view_single_func

def display_menu():
    """Clean and attractive main menu"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" + "═" * 55)
    print("    🎓 Student Marks Manager - Main Menu")
    print("═" * 55)
    print("1. Add Student")
    print("2. Modify Student")
    print("3. Delete Student")
    print("4. View All Students")
    print("5. View Individual Student")
    print("6. Exit")
    print("═" * 55)

def main():
    while True:
        display_menu()
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == "1":
            try:
                roll_no = int(input("Enter Roll No (3 digits): "))
                name = input("Enter Name: ")
                marks = int(input("Enter Marks (0-100): "))
                add_func('marks.txt', roll_no, name, marks)
            except ValueError:
                print("❌ Invalid input! Please enter numbers only.")

        elif choice == "2":
            roll_no = int(input("Enter Roll No to modify: "))
            marks = int(input("Enter new Marks (0-100): "))
            modify_func('marks.txt', roll_no, marks)

        elif choice == "3":
            roll_no = int(input("Enter Roll No to delete: "))
            delete_func('marks.txt', roll_no)

        elif choice == "4":
            view_all_func('marks.txt')

        elif choice == "5":
            roll_no = int(input("Enter Roll No to view: "))
            view_single_func('marks.txt', roll_no)

        elif choice == "6":
            print("\n👋 Exiting Student Marks Manager. Goodbye!")
            break

        else:
            print("\n❌ Invalid choice! Please enter 1-6.")

if __name__ == "__main__":
    main()
