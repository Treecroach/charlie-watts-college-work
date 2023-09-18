def triangle_area():
    base = int(input("please input the length of the base of your triangle"))
    height = int(input("please input the height of your triangle"))
    area = base*height/2
    print("the area of your triangle is ", area)
    
def power_calculator():
    voltage = int(input("please enter the voltage"))
    current = int(input("please enter the current"))
    power = voltage*current
    print("the power is",power)

def two_numbers():
    num1 = int(input("please enter your first number"))
    num2 = int(input("please enter your second number"))
    answer = num1+num2
    print(num1,"+",num2,"=",answer)

def age_to_days():
    age = int(input("please enter your age"))
    days = age*365
    print(age,"years = ",days,"days")

age_to_days()

