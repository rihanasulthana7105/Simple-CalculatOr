#To build simple calculator
def calculator():
    print("Simple Calculator")
    #Loop to allow continuous calculations
    while True:
    #Taking user input for numbers or operands with exception handling to avoid value error
        try:
            operand1=float(input("Enter first operand: "))
            operand2=float(input("Enter second operand: "))
        except ValueError:
            print("Invalid input!Please enter numerical values.")
            continue
        #Display available operations
        print("\nSelect Operation: ")
        print("1.Addition (+)")
        print("2.Subtraction (-)")
        print("3.Multiplication (*)")
        print("4.Division (/)")
        print("5.Modulus (%)")
        operation=input("\nEnter operation:-+,-,*,/,% (or) name:-e.g., addition : ").strip().lower()
        #Perform calculation and handle division by zero using try/except 
        try:
            if operation in ['1','+','addition']:
                result=operand1+operand2
                print("Result: ",result)
            elif operation in ['2','-','subtraction']:
                result=operand1-operand2
                print("Result: ",result)
            elif operation in ['3','*','multiplication']:
                result=operand1*operand2
                print("Result: ",result)
            elif operation in ['4','/','division']:
                result=operand1/operand2
                print("Result: ",result)
            elif operation in ['5','%','modulus']:
                result=operand1%operand2
                print("Result: ",result)
            else:
                print("Invalid operation selected.")
        except ZeroDivisionError:
            print("Error:Division or Modulus by zero is not allowed!")
        #Ask user if they wan to continue to peform
        again= input("\nDo you want to continue?(yes/no): ")
        if again not in ['y','yes']:
            print("Thank you for using calculator.Goodbye!")
            break#Exit the loop
#calling the function directly to execute
calculator()

            