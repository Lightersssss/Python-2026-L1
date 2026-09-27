students = []
courses = []
marks = {}

def input_students():
    num = int(input("Input number of students in a class: "))
    for _ in range(num):
        s_id = input("Student ID: ")
        name = input("Student name: ")
        dob = input("Student DoB: ")
        students.append({"id": s_id, "name": name, "dob": dob})

def input_courses():
    num = int(input("Input number of courses: "))
    for _ in range(num):
        c_id = input("Course ID: ")
        name = input("Course name: ")
        courses.append({"id": c_id, "name": name})

def input_marks():
    while True:
        c_id = input("Select a course ID to input marks (or 'q' to quit): ")
        if c_id == 'q':
            break
        if c_id not in [course['id'] for course in courses]:
            print("Invalid course ID.")
            continue
        marks[c_id] = {}
        for s in students:
            mark = float(input(f"Input mark for student {s['name']}: "))
            marks[c_id][s['id']] = mark

def list_students():
    print("--- Student List ---")
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | DoB: {s['dob']}")

def show_marks():
    while True:
        c_id = input("Input course ID to show marks (or 'q' to quit): ")
        if c_id == 'q':
            break
            
        if c_id in marks:
            for s in students:
                s_id = s['id']
                print(f"Student {s['name']}: {marks[c_id].get(s_id, 'No mark yet')}")
        else:
            print("No mark data for this course.")
# --- Run the program ---
# Uncomment the lines below to test each function
# input_students()
# input_courses()
# input_marks()
# list_students()
# show_marks()
