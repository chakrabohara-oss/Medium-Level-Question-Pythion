student = {
    "name": "Ram",
    "age": 19,
    "course": "BCA",
    "marks": 78
}

print("student Information: ")
print(student)

student["marks"] = student["marks"] + 5

if student["marks"] >= 40:
    student["status"] = "Pass"
else:
    student["status"] = "Fail"

# Display updated dictionary
print("\nUpdated Student Information:")
print(student)