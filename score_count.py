students = [{'name': 'Alice', 'score': [85, 90, 78]},
           {'name': 'Bob', 'score': [92, 88, 95]},
           {'name': 'David', 'score': [88,23,43]},]
for student in students:
    name = student['name']
    scores = student['score']
    total_score = sum(scores)
    print(f"{name} 's total score: {total_score}")
    average_score = sum(scores) / len(scores)
    print(f"{name} 's average: {average_score:.2f}")
top_student = max(students, key=lambda x: sum(x['score']))
print(f"Top student: {top_student['name']}, total score: {sum(top_student['score'])}")