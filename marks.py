students = {}  # name -> list of marks
def add_student():
    name = input("Student name: ").strip()
    marks_input = input("Enter marks separated by spaces (e.g. 78 85 90): ")

    try:
        marks = [int(m) for m in marks_input.split()]
    except ValueError:
        print("Invalid input, marks must be numbers.\n")
        return

    students[name] = marks
    print(f"Added {name} with marks {marks}.\n")
def grade_for(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"
def show_report():
    if not students:
        print("No students added yet.\n")
        return

    print(f"\n{'Name':<15}{'Average':<10}{'Grade'}")
    print("-" * 32)
    for name, marks in students.items():
        avg = sum(marks) / len(marks)
        print(f"{name:<15}{avg:<10.1f}{grade_for(avg)}")
    print()
def show_topper():
    if not students:
        print("No students added yet.\n")
        return

    # Find the student with the highest average using max() + a lambda key
    averages = {name: sum(marks) / len(marks) for name, marks in students.items()}
    top_name = max(averages, key=averages.get)
    print(f"Topper: {top_name} with average {averages[top_name]:.1f}\n")
def main():
    menu = """
Student Marks Tracker
1. Add student
2. Show report (averages + grades)
3. Show topper
4. Quit
"""
    while True:
        print(menu)
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            show_report()
        elif choice == "3":
            show_topper()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")
if __name__ == "__main__":
    main()