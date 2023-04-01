'''1.Write a menu driven program to store the students details(rno,name,mark) as a list of tuples.The menu has the following options 
add-adding students details
remove-remove the details by giving roll number
search-search and display the details by giving roll number
max-display the details of the students with highest mark
student_details = []'''

def add_student():
    rno = input("Enter roll number: ")
    name = input("Enter name: ")
    mark = input("Enter mark: ")
    student_details.append((rno, name, mark))
    print("Student added successfully!")

def remove_student():
    rno = input("Enter roll number to remove: ")
    for student in student_details:
        if student[0] == rno:
            student_details.remove(student)
            print("Student removed successfully!")
            return
    print("Student with roll number {} not found.".format(rno))

def search_student():
    rno = input("Enter roll number to search: ")
    for student in student_details:
        if student[0] == rno:
            print("Roll Number: {}\nName: {}\nMark: {}".format(student[0], student[1], student[2]))
            return
    print("Student with roll number {} not found.".format(rno))

def max_student():
    if len(student_details) == 0:
        print("No students found!")
        return
    max_mark = max([int(student[2]) for student in student_details])
    max_students = [student for student in student_details if int(student[2]) == max_mark]
    for student in max_students:
        print("Roll Number: {}\nName: {}\nMark: {}".format(student[0], student[1], student[2]))

while True:
    print("\nMenu:")
    print("1. Add student")
    print("2. Remove student")
    print("3. Search student")
    print("4. Display student(s) with highest mark")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        add_student()
    elif choice == '2':
        remove_student()
    elif choice == '3':
        search_student()
    elif choice == '4':
        max_student()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Try again.")
        
        
1. Write a program to do basic set operations

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1.union(set2)   # Union of two sets
intersection = set1.intersection(set2)   # Intersection of two sets
difference = set1.difference(set2)   # Set difference of set1 - set2
symmetric_difference = set1.symmetric_difference(set2)   # Symmetric difference of two sets

print("Set 1:", set1)
print("Set 2:", set2)
print("Union:", union)
print("Intersection:", intersection)
print("Set Difference (Set 1 - Set 2):", difference)
print("Symmetric Difference:", symmetric_difference)

#2. The simple way to remove duplicate elements from a list is to convert into a set and then convert back to list.This program will completely remove duplicate elements without keeping any copy.
# Define a sample list with duplicate elements
my_list = [1, 2, 3, 2, 4, 3, 5, 6, 1]

unique_set = set(my_list)

unique_list = list(unique_set)

print("Original List:", my_list)
print("List without duplicates:", unique_list)
