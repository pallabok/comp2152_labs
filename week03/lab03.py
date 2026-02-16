# start_python_file.py
# Lab 03 – Python Collections Practice
# Covers: Lists, Tuples, Sets, Dictionaries

# ============================================================
# Question 1: Student Grades List
# ============================================================
print("=" * 50)
print("Question 1: Student Grades List")
print("=" * 50)
grades = [85, 92, 78, 95, 88]
grades.append(90)
print(grades)
grades.sort()
print("Sorted Grades:", grades)
print("Highest Grades:", grades[-1])
print("Lowest Grades:", grades[0])
print("Total Grades:", len(grades))
print()

# ============================================================
# Question 2: Shopping Cart
# ============================================================
print("=" * 50)
print("Question 2: Shopping Cart")
print("=" * 50)
cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]
apple_count = cart.count("apple")
print("Number of apples", apple_count)
milk_position = cart.index("milk")
print("Milk Position:", milk_position)
cart.remove("apple")
removed_item = cart.pop()
print("Removed item using pop: ", removed_item )
print("Is there a banana in the cart?", "banana" in cart)
print("Final cart:", cart)
print()

# ============================================================
# Question 3: Coordinate System (Tuples)
# ============================================================
print("=" * 50)
print("Question 3: Coordinate System")
print("=" * 50)
point1 = (3,5)
point2 = (7,2)
print("Point1:", point1)
print("Point2:", point2)
x1, y1 = point1
x2, y2  = point2
print("x1 =", x1, ", y1 =", y1)
print("x2 =", x2, ", y2 =", y2)
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) **0.5
print("Distance between points:", distance)
print()

# ============================================================
# Question 4: Class Attendance (Sets)
# ============================================================
print("=" * 50)
print("Question 4: Class Attendance")
print("=" * 50)
monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}
monday_class.add("Grace")
print("Monday class: ", monday_class)
print("Wednesday class: ", wednesday_class)
print("Attended both classes: ", monday_class & wednesday_class)
print("Attended either classes: ", monday_class | wednesday_class)
print("Only attended Monday class: ", monday_class - wednesday_class)
print("Only attended one class: ", monday_class ^ wednesday_class)
all_Students = monday_class | wednesday_class
print("Is Monday subset of all students? ", monday_class <= all_Students)
print()

# ============================================================
# Question 5: Contact Book (Dictionaries)
# ============================================================
print("=" * 50)
print("Question 5: Contact Book")
print("=" * 50)
contacts  = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}
print("Alice's number: ", contacts["Alice"])
contacts["Diana"] = "555-4321"
print("Contacts after adding Diana: ", contacts)
contacts["Bob"] = "555-0000"
print("Contacts after updating Bob: ", contacts)
del contacts["Charlie"]
print("Contacts after deleting Charlie: ", contacts)
print("All names: ", contacts.keys())
print("All numbers: ", contacts.values())
print("Total Contacts: ", len(contacts))
print()