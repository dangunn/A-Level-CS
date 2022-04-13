def get_grades_stub():
    return [20, 30, 80]

def calc_average():
    grades = get_grades_stub()

    t = 0
    for g in grades:
        t = t + g

    print(t/len(grades))