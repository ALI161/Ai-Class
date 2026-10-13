scores = {
    "Ali": 18,
    "Sara": 20,
    "Reza": 9,
    "Mina": 14,
    "Omid": 11.5
}

passed_students = []

for name, score in scores.items():
    if score >= 17:
        status = "Excellent"
    elif score >= 14:
        status = "Good"
    elif score >= 10:
        status = "Pass"
    else:
        status = "Fail"
    print(name, ":", score, "->", status)

    if score >= 10:
        passed_students.append(name)
print("Passed students:", passed_students)

average = sum(scores.values()) / len(scores)
print("Class average:", average)

top_student = max(scores, key=scores.get)
print("Top student:", top_student)
