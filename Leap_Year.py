#Leap Year Function

def Leap_Year(year):
    if (year % 4 == 0 and year % 100 !=0) or (year % 400 ==0):
        print(True)
        return
    print(False)

Leap_Year(2001)