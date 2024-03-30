while True:
    Num1=int(input('pleas Enter your number1:'))
    Num2=int(input('pleas Enter your number2:'))
    Myop=(input('pleas Enter your operator:'))
    def calculator():
        if Myop=='+':
            print(Num1+Num2)
        elif Myop=='-':
            print(Num1-Num2)
        elif Myop=='*':
            print(Num1*Num2)
        elif Myop=='/':
            print(Num1/Num2)
        else:
            print('your operator is wromg!!! ')
    calculator()
