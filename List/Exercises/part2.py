n =eval(input("Enter number of items: "))
calender = {}
while True:
    month = input("Enter month: ")
    if month == "q":
        break
    else:
        days = eval(input("Enter number of days in month: "))
        calender[month]= days
        
if calender[month] == 31:
    print(calender[month])

