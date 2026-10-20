#Leap Year Function

def Leap_Year(year):
    if (year % 4 == 0 and year % 100 !=0) or (year % 400 ==0):
        return True
    return False

def Leap_Year_statement(year):
    if year >= 0:
        DeadCode = True
    if (year % 4 == 0 and year % 100 !=0) or (year % 400 ==0):
        return True
    return False

def Leap_Year_condition(year):
    if year >= 0:
        DeadCode = True
    a = (year%4 == 0)
    b = (year%100 !=0)
    c = (year%400 == 0)
    return (a and b) or c

def Leap_Year_BranchCondition(year):
    a = (year%4 == 0)
    b = (year%100 !=0)
    c = (year%400 == 0)
    #a and b are not independent
    if (a and b) or c:
        return True
    else:
        return False