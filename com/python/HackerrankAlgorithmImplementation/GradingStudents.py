def solveGrades(grades):
    for i in range(0, len(grades)):
        if grades[i] < 0 or grades[i] > 100:
            return 0
        if grades[i] < 38:
            print grades[i]
        else:
            print calculate_next_multiple(grades[i])


def calculate_next_multiple(x):
    n1 = int(x/5)
    n2 = n1 + 1
    prod = n2*5
    if prod-x < 3:
        x = prod
    else:
        x = x
    return x

grades = [73,67,38,33]
solveGrades(grades)

