grades ={"Vinay": (99,99,99,99),
         "Divvyam": (55,66,77,77),
         "Devang": (1,2,99,100)
}
passed_students =set()
for student,score in grades.items():
    average = sum(score) / len(score)

    if average >= 75:
        print(f"{student} → Average: {average:.1f} → Pass")
        passed_students.add(student)
    else:
        print(f"{student} → Average: {average:.1f} → Fail")

print("\nStudents who passed:", passed_students)