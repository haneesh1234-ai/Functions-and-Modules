#caluclator🧮

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

print("Select one of the operation below (1/2/3/4)")

print("1. Addition")

print("2. Subtraction")

print("3. Multiplcation")

print("4. Division")

num1 = int(input("enter the first number : "))
num2 = int(input("enter the second number : "))
choice = input("enter your choice of operation : ")
if choice == "1":
    print("result : ",add(num1,num2))
elif choice == "1":
    print("result : ",sub(num1,num2))
elif choice == "1":
    print("result : ",mul(num1,num2))
elif choice == "1":
    print("result : ",div(num1,num2))