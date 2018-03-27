def calculator(x, b, y):
    if b == '+':
        print(x,"+",y,"=", x + y)
    elif b == '-':
        print(x,"-",y,"=", x - y)
    elif b == '*':
        print(x,"*",y,"=", x * y)
    elif b == '/':
        print(x,"/",y,"=", x / y)
    else:
        print("Invalid input")
    return
