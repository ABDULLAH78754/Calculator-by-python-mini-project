print("*********** Welcome Calculator by Python ***********")
num =float(input("Enter Number: "))
Operator = ("+" , "-" , "*" , "/" , "%" , "r" , "re" , "e")
result=num
exit = False
while True:
    op =input("Enter Operator ( + - * / %, r to reset, re to result, e to exit): ")
    if op in Operator :
        if op == "e":
            print("Exiting the calculator. Goodbye!")
            exit = True
            break
        elif op == "+":
            no= float(input("Enter Number: "))
            result +=no
        elif op == "-":
            no= float(input("Enter Number: "))
            result -=no
        elif op == "*":
            no= float(input("Enter Number: "))
            result *=no
        elif op == "/":
            if no == 0:
                print("Error: Division by zero is not allowed.")
                break
            else:
                no= float(input("Enter Number: "))
                result /=no
        elif op == "%":
            no= float(input("Enter Number: "))
            result %=no
        elif op == "r":
            result = 0
            print("Calculator reset.")
        elif op == "re":
            print(f"Result: {result}.")
    else:
        print("Invalid Input! .Try again")