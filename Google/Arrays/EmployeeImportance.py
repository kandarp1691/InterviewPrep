def getImportance(employees, id):
    """
    :type employees: Employee
    :type id: int
    :rtype: int
    """
    imp = 0
    subordinates = None
    for employee in employees:
        if employee[0] == id:
            imp = employee[1]
            subordinates = employee[2]
            if len(subordinates) == 0:
                return imp
    for employee in employees:
        if employee[0] in subordinates:
            imp = employee[1] + imp
    return imp

employees = [[1,2,[2]], [2,3,[]]]
id = 2

print getImportance(employees, id)