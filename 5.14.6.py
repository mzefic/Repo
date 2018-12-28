mark = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

def calc_exam(x):
    if x >= 75:
        grade = "First"
    elif ((x >= 70) and (x <= 75)):
        grade = "Upper Second"
    elif ((x >= 60) and (x <= 70)):
        grade = "Second"
    elif ((x >= 50) and (x <= 60)):
        grade = "Third"
    elif ((x >= 45) and (x <= 50)):
        grade = "F1 Supp"
    elif ((x >= 40) and (x <= 45)):
        grade = "F2"
    elif x < 40:
        grade = "F3"
    return print(grade)

i = float

for i in mark:
    calc_exam(i)