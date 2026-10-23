# Common Big Program - Student Management System

students = {}

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = []
    for i in range(3):
        m = int(input(f"Enter Mark {i+1}: "))
        marks.append(m)
    
    total = sum(marks)
    avg = total / 3
    
    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    else:
        grade = "Fail"
    
    students[roll] = {"name": name, "marks": marks, "total": total, "avg": avg, "grade": grade}
    print("Student Added Successfully!\n")

def display_all():
    print("\n--- ALL STUDENTS ---")
    for roll, data in students.items():
        print(f"Roll: {roll} | Name: {data['name']} | Total: {data['total']} | Avg: {data['avg']:.2f} | Grade: {data['grade']}")
    print()

def search_student():
    roll = input("Enter Roll No to search: ")
    if roll in students:
        s = students[roll]
        print(f"Found - {s['name']}, Total: {s['total']
