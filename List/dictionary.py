# dictionary = {"car":["benz","bmw","ford"]}
# print(dictionary.get("car"))
# print(dictionary["car"])
# car = {"model":"bmw",
#         "year":1922
# }
# print(car.get("model"))
# car.update({"year": 1945})
# print(car.get("year"))
# car = {"car1":{"model":"ford"},
#        "car2":{"model":"bmw"}
# }
# print(car["car1"]["model"])
# car = {"car1":{"model":"ford",
#                "year":1936},
#        "car2":{"model":"bmw",
#                "year":1945}
# }
# print(car["car1"]["model"])
# def limp(name):
#      name = input("Enter your name")
#      print("Happy Birthday "+name )  
# limp("name")
# def sum(sum_1):
#     num1=eval(input("Enter value1"))
#     num2=eval(input("Enter value 2"))
#     sum_1= num1+num2
#     print(sum_1)
# sum("sum_1") 
# def divide(divide_1):
#     num1=eval(input("Enter the value1"))
#     num2=eval(input("Enter the value2"))
#     divide_1= num1/num2
#     print(divide_1)
# divide("divide_1")
def remain(remain_1):
    num=eval(input("Enter your value"))
    remain_1=num%2
    print(remain_1)
remain("remain_1") 