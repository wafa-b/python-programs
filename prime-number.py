number = int(input("Please Enter number to check if prime or not: "))

if number <= 1:
    print('Not prime Number')
else:
    for i in range(2,number):
        if (number % i) == 0:
            print(number,'is Not Prime Number')
            break
    else:
        print(number,'is Prime Number')
