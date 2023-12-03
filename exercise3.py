def calculate():
    num1 = input("Enter X number: ")
    num1=int(num1)

    num2 = input("Enter Y number: ")
    num2 = int(num2)
    operation = int(input("enter 1 for addition, 2 to subtract, 3 to multily and 4 for division: "))

    if num1 % 2 == 0:
        print (num1," is Even ")
    else:
        print(num1," is Odd ")

    if num2 % 2 == 0:
        print(num2, " is Even ")
    else:
        print(num2, " is Odd ")

    if operation == 1:
        print("x + y = ", num1 + num2)
    elif operation ==2:
        print("X - Y = ", num1 - num2)
    elif operation ==3:
        print("X * Y = ", num1 * num2)
    else:
        print("X / Y = ", num1/num2)

if __name__=="__main__":
    calculate()