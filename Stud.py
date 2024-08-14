grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print("Кол-во студентов:",len(students))
print('Кол-во оценок:', len(grades))
print('Совпадает ли кол-во студентов и оценок:', len(grades) == len(students))
students = sorted(students)
grades_m = []
for num in grades:
        (s)=sum(num)/len(num)
        grades_m.append(s)
result = dict(zip(students,grades_m))
print("Средний балл:", result)