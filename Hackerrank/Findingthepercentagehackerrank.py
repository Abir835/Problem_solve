n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    score = list(map(float, line))
    student_marks[name] = score

queryName = input()
totalScore = 0
for i in student_marks[queryName]:
    totalScore += i
print(format(totalScore/3, '.2f'))

