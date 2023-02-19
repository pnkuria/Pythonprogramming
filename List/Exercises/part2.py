calender = {}
while True:
    month = input("Enter month: ")
    if month == 12:
        days = eval(input("Enter number of days in month: "))
        calender[month]= days
        break
print(calender)