try:
    number = int(input("please enter number: "))
    result = number / 2
    print(result)

    fo_obj = open("test.txt","r")
    data = fo_obj.read()
    fo_obj.close()
except FileNotFoundError:
    print('THe File Not Found')
except TypeError:
    print('Please check the input format')
except Exception as e:
    print(e)
else:
    print('No error')
