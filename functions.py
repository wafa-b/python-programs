def add(num1,num2):
    result=num1+num2
    return result

def sub(num1,num2):
    result=num1-num2
    return result

if __name__ == "__main__":
    num1 = int(input("please number 1: "))
    num2 = int(input("please number 2: "))
    res=add(num1,num2)
    print(num1,'+',num2,'=',res)
    res2=sub(res,num2)
    print(num1,'-',num2,'=',res2)

