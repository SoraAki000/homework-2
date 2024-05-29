# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
print("-------- Задание 1. --------")
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
count_names = {}
for student in students:
    if student["first_name"] in count_names:
        count_names[student['first_name']] += 1
    else:
        count_names[student['first_name']] = 1
for name, count in count_names.items():
    print(f"{name}: {count}")

# Задание 2
# Дан список учеников, нужно вывести самое часто повторяющееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
print("-------- Задание 2. --------")
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
count_names, temp = {}, ["name", 0]
for student in students:
    if student["first_name"] in count_names:
        count_names[student['first_name']] += 1
    else:
        count_names[student['first_name']] = 1
for student, count in count_names.items():
    if count > temp[1]:
        temp = [student, count]
print(f"Самое частое имя среди учеников: {temp[0]}")


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша
print("-------- Задание 3. --------")
school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],
    [  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
count_names, often_per_class = [], []
for school_class in school_students:
    count_class = {}
    for student in school_class:
        if student["first_name"] in count_class:
            count_class[student['first_name']] += 1
        else:
            count_class[student['first_name']] = 1
    count_names.append(count_class)
for school_class in count_names:
    temp = ["name", 0]
    for student, count in school_class.items():
        if count > temp[1]:
            temp = [student, count]
    often_per_class.append(temp[0])
for student in often_per_class:
    print(f"Самое частое имя в классе {often_per_class.index(student)+1}: {student}")


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2
print("-------- Задание 4. --------")
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
gender_per_class = []
for school_class in school:
    male, female = 0, 0
    for student in school_class["students"]:
        if is_male[student["first_name"]]:
            male += 1
        else:
            female += 1
    gender_per_class.append({school_class["class"]: [female, male]})
for school_class in gender_per_class:
    for class_name, genders in school_class.items():
        print(f"Класс {class_name}: девочки {genders[0]}, мальчики {genders[1]}")


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
print("-------- Задание 5. --------")
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
genders_per_class = []
for school_class in school:
    male, female = 0, 0
    for student in school_class["students"]:
        if is_male[student["first_name"]]:
            male += 1
        else:
            female += 1
    genders_per_class.append({school_class["class"]: [female, male]})
temp_male, temp_female = ["class", 0], ["class", 0]
for school_class in genders_per_class:
    for class_name, genders in school_class.items():
        if genders[1] > temp_male[1]:
            temp_male = [class_name, genders[1]]
        if genders[0] > temp_female[1]:
            temp_female = [class_name, genders[0]]
print(f"Больше всего мальчиков в классе {temp_male[0]}")
print(f"Больше всего девочек в классе {temp_female[0]}")
