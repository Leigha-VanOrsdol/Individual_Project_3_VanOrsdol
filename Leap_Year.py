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
    if True:
        pass
    else:
        print("for branch")
    a = (year%4 == 0)
    b = (year%100 !=0)
    c = (year%400 == 0)
    return (a and b) or c