# person = {
#     "name":"cathy",
#     "age":34,
#     "pets":{"dog":"charlie",
#             "cat":"minnie"
#             }
# }

# print(person["pets"]["dog"])
# profile ={}
# profile["username"]=input("Enter user_name")
# profile["age"]=input("Enter age")
# profile["email"]=input("enter email")

# print(profile)
profile = {}
def register():
    user_name = input("Enter name:")
    email = input("Enter email:")
    password = input("Enter password:")
    profile["username"] = user_name
    profile["email"]= email
    profile["password"] = password
    
def get_profile():
    print(profile)
def change_username():
    new_username=input("Enter new user_name:")
    profile["username"]= new_username
register()
get_profile()
change_username()
get_profile()