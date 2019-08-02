try:
    file_obj = open("foo.txt","r")
    data = file_obj.read()
    file_obj.close()
except FileNotFoundError:
    print('Sorry, File does not Found')
else:
    print(10*10)
finally:
    print('in everything')

