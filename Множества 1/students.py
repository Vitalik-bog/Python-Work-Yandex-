students_all = [set([input() for _ in range(int(input()))]) for j in range(int(input()))]
result_students = students_all[0].intersection(*students_all[1:])
[print(student) for student in sorted(list(result_students))]