while True:
    num1=int(input('pleas Enter your number1:'))
    num2=int(input('pleas Enter your number2:'))
    myop=(input('pleas Enter your operator:'))
    def calculator():
        if myop=='+':
            print(num1+num2)
        elif myop=='-':
            print(num1-num2)
        elif myop=='*':
            print(num1*num2)
        elif myop=='/':
            print(num1/num2)
        else:
            print('your operator is wromg!!! ')
    calculator()