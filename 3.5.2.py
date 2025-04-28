# Student Information
print("Name: Soronnadi Chidiebere Prince")
print("Course: COS 201 Practical")
print("Reg No: 20231410912")
print("Dept: IFT\n")

# 1. Create a tuple containing the names of five students in your class
students = ("Destiny", "Festus", "Legit", "Richard", "Emmanuel")
print("All students:", students)

# 2. Access and print the name of the second student
print("Second student:", students[1])

# 3. Attempt to change the name of the first student (observe the result)
try:
    students[0] = "Alex"
except TypeError as error:
    print("Error when trying to change the first student:", error)

# 4. Unpack the tuple into three separate variables and print them
student1, student2, student3, _, _ = students  # Using _ to ignore the rest
print("Unpacked students:")
print(student1)
print(student2)
print(student3)
    