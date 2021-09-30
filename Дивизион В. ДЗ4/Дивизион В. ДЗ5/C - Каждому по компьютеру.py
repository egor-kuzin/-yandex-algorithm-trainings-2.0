with open('input.txt', 'r') as fin:
    groups, classrooms = map(int, fin.readline().split())
    students = list(map(int, fin.readline().split()))
    comps = list(map(int, fin.readline().split()))
del fin
del groups
del classrooms


students_sorted = []
comps_sorted = []

for _, student in enumerate(students):
    students_sorted.append([_, student, 0])
students_sorted = sorted(students_sorted, key=lambda x: x[1])
del student
del students

for _, comp in enumerate(comps):
    comps_sorted.append([_, comp])
comps_sorted = sorted(comps_sorted, key=lambda x: x[1])
del _
del comp
del comps

counter = 0
pos = 0

for student in students_sorted:
    for index in range(pos, len(comps_sorted)):
        if student[1] <= comps_sorted[index][1] - 1:
            student[2] = comps_sorted[index][0] + 1
            counter += 1
            break
    pos = index + 1
del pos
del comps_sorted
del index
del student

a = [x[2] for x in sorted(students_sorted, key=lambda x: x[0])]
del students_sorted

print(counter)
print(*a)

