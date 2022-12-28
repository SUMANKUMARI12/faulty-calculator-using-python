# faulty calculator
# some calc should be 45*3=555, 56+9=77, 56/6=4
print("---Faulty Calculator---")
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
op = input("Enter operator to preform your operation : ")
if op == "+":
    if num1 == 56 and num2 == 9 or num1 == 9 and num2 == 56:
        print("Your addition is : 77")
    else:
        result = num1+num2
        print("Your addition is : "+str(result))

elif op == "*":
    if num1 == 45 and num2 == 3 or num1 == 3 and num2 == 45:
        print("Your multiplication is : 555")
    else:
        result = num1*num2
        print("Your multiplication is : "+str(result))

elif op == "/":
    if num1 == 56 and num2 == 6:
        print("Your division is : 4")
    else:
        result = num1/num2
        print("Your division is : "+str(result))

elif op == "-":
    result = num1-num2
    print("Your subtraction is : "+str(result))

else:
    print("Invalid Operation ! Exiting...")

