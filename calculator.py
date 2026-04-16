print("1-ADDITION")
print("2-SUBTRACTION")
print("3-MULTIPLICATION")
print("4-DIVISION")

option= float(input("Enter your choice:  " ))

if option in [1,2,3,4]:

    num1 = float(input("Enter first number:  "))
    num2 = float(input("Enter second number:  "))

    if option==1:
        result= num1 + num2
    elif option==2 :
        result=  num1 - num2
    elif option==3 :
        result= num1 * num2
    elif option==4 :
        result= num1 /num2
        
    print("The result of this operation is ",result)



else:
    print("Invalid operation entered")


