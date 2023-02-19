n =eval(input("Enter number of items: "))
calender = {}
while True:
    month = input("Enter month: ")
    if month == 12:
        break
    else:
        days = eval(input("Enter number of days in month: "))
        calender[month]= days
        
    for i in range(n):
        print(calender)