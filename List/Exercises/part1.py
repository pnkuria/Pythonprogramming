dict = {}
while True:
    for q in range (10):
        product = input("Enter product name")
        if product == q:
            break
        else:
            price = eval(input("Enter price of product"))
            dict[product]= price
    while True:
        name = input("Enter product name:")
        if name == "q":
            break
        else:
            if name not in dict:
                print("Not valid")
            else:
                print("The price of product is:",dict[name])
    while True :
        if price >100:
            print(dict)