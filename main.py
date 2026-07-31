def grade_marks(marks):
    if marks >= 90:
        return "O"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 55:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

# --- Add Student ---
def add_student(filename, roll_no, name, marks):
    if not all(c.isdigit() for c in str(roll_no)) or len(str(roll_no)) != 3:
        print("Error: Roll number must be a 3-digit integer.")
        return
    if not all(c.isalpha() or c.isspace() for c in name):
        print("Error: Name must contain only alphabetic characters and spaces.")
        return
    if marks < 0 or marks > 100:
        print("Error: Marks must be between 0 and 100.")
        return

    grade = grade_marks(marks)

    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []

    new_lines = []
    exists = False
    skip = False

    for line in lines:
        if line.startswith("Roll No:") and str(roll_no) in line:
            exists = True
            choice = input(f"⚠️ Roll No {roll_no} already exists. Replace record? (y/n): ")
            if choice.lower() == "y":
                new_lines.append(f"Roll No: {roll_no}\nName: {name}\nMarks: {marks}\nGrade: {grade}\n\n-------------------------\n\n")
                skip = True
                print(f"✅ Record for Roll No {roll_no} replaced.")
            else:
                skip = False
                print(f"❌ Record for Roll No {roll_no} left unchanged.")
        elif skip and line.strip() == "-------------------------":
            skip = False
        else:
            if not skip:
                new_lines.append(line)

    if not exists:
        new_lines.append(f"Roll No: {roll_no}\nName: {name}\nMarks: {marks}\nGrade: {grade}\n\n-------------------------\n\n")
        print(f"✅ Record for Roll No {roll_no} added successfully with Grade {grade}.")

    with open(filename, "w") as f:
        f.write("".join(new_lines))

# --- Modify Student ---
def modify_student(filename, roll_no, new_marks):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Error: File not found.")
        return

    new_lines = []
    exists = False
    skip = False

    for line in lines:
        if line.startswith("Roll No:") and str(roll_no) in line:
            exists = True
            choice = input(f"⚠️ Roll No {roll_no} found. Modify record? (y/n): ")
            if choice.lower() == "y":
                grade = grade_marks(new_marks)
                new_lines.append(f"Roll No: {roll_no}\nMarks: {new_marks}\nGrade: {grade}\n\n-------------------------\n\n")
                skip = True
                print(f"✅ Record for Roll No {roll_no} modified.")
            else:
                skip = False
                print(f"❌ Record for Roll No {roll_no} left unchanged.")
        elif skip and line.strip() == "-------------------------":
            skip = False
        else:
            if not skip:
                new_lines.append(line)

    if not exists:
        print(f"❌ Roll No {roll_no} not found.")
    else:
        with open(filename, "w") as f:
            f.writelines(new_lines)

# --- Delete Student ---
def delete_student(filename, roll_no):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Error: File not found.")
        return

    new_lines = []
    exists = False
    skip = False

    for line in lines:
        if line.startswith("Roll No:") and str(roll_no) in line:
            exists = True
            choice = input(f"⚠️ Roll No {roll_no} found. Delete record? (y/n): ")
            if choice.lower() == "y":
                skip = True
                print(f"✅ Record for Roll No {roll_no} deleted.")
            else:
                skip = False
                new_lines.append(line)
                print(f"❌ Record for Roll No {roll_no} kept.")
        elif skip and line.strip() == "-------------------------":
            skip = False
        else:
            if not skip:
                new_lines.append(line)

    if not exists:
        print(f"❌ Roll No {roll_no} not found.")
    else:
        with open(filename, "w") as f:
            f.writelines(new_lines)

# --- View All Students ---
def view_all_students(filename):
    try:
        with open(filename, "r") as f:
            content = f.read()
            if content.strip() == "":
                print("⚠️ No records found.")
            else:
                print("📘 Student Records:\n")
                print(content)
    except FileNotFoundError:
        print("Error: File not found.")

# --- View Individual Student ---
def view_student(filename, roll_no):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Error: File not found.")
        return

    found = False
    record = []
    for line in lines:
        if line.startswith("Roll No:") and str(roll_no) in line:
            found = True
            record.append(line)
        elif found:
            record.append(line)
            if line.strip() == "-------------------------":
                break

    if found:
        print("📘 Student Record:\n")
        print("".join(record))
    else:
        print(f"❌ Roll No {roll_no} not found.")
