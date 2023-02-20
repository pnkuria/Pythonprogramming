import operators
import others
import trig
operator = input("Enter operator: ")
if operator == "cube":
    num = eval(input("Enter number: "))
    print(others.cube(num))
elif operator == "square":
    num = eval(input("Enter number: "))
    print(others.square(num))
elif operator == "sine":
    angle = eval(input("Enter your angle in degrees: "))
    print(trig.get_sine(angle))
elif operator == "tan":
    angle = eval(input("Enter your angle in degrees: "))
    print(trig.get_tangent(angle))
elif operator == "cos":
    angle = eval(input("Enter your angle in degrees: "))
    print(trig.get_cosine(angle))
else:
    num1 = eval(input("Enter number 1: "))
    num2 = eval(input("Enter number 2: "))

    if operator == "+":
        n= operators.add(num1,num2)
        print(n)
    elif operator == "-":
        print(operators.add(num1,num2))
    elif operator == "/":
        print(operators.divide(num1,num2))
    elif operator == "*" or "x" or "X":
        print(operators.multiply(num1,num2))
