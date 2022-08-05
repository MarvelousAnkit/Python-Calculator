print("+ Add \n- Subtract \n* Multiplication \n /Divide")
num_1 = int(input("Enter a value 1  :"))
num_2 = int(input("Enter a value 2  :"))
opr = input("Enter The operation (+,-,*,/) :")

if (opr=="+"):
    print(num_1+num_2)
elif (opr=="-"):
    print(num_1-num_2)
elif(opr=="*"):
    print(num_1*num_2)
elif(opr=="/"):
    print(num_1/num_2)
else:
    print("Invalid Operation")