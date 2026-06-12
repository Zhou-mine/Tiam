def getNumber():
    n,m = map(float,input("输入数字间隔使用空格:").split())
    return n,m

def plusMethud(num1,num2):
    print("结果为:")
    print(f"{num1}+{num2}=",num1+num2)

def dMethud(num1,num2):
    print("结果为:")
    print(f"{num1}-{num2}=",num1-num2)

def sMethud(num1,num2):
    print("结果为:")
    print(f"{num1}x{num2}=",num1*num2)

def fMethhud(num1,num2):
    if num2 == 0:
        print("value number2 error")
        return 0
    else:
        print("结果为:")
        print(f"{num1}/{num2}=",f"{num1/num2:.4f}")

def menu():
    while True:
        print("==========culculator==========")
        print("运算方法:")
        print("加法:+")
        print("减法:-")
        print("乘法:x")
        print("除法:/")
        print("==========exit type end=======")
        sign = str(input("选择运算方法:"))
        if sign == 'end':
            print("\033[0m")
            break
        n,m = getNumber()
        print("\033[34m")
        if sign == '+':
            plusMethud(n,m)
        elif sign == '-':
            dMethud(n,m)
        elif sign == 'x':
            sMethud(n,m)
        elif sign == "/":
            fMethhud(n,m)
        print("\033[0m")

def main():
    menu()

if __name__ == "__main__":
    main()
