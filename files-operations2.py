# file_obj = open("test.txt","w")
# file_obj.write('TechCampus')
#
# file_obj.close()

# file_obj = open("test.txt","a")
# file_obj.write('\nMy name is wafa')
#
# file_obj.close()

file_obj = open("test.txt","r")
data = file_obj.read()
print(data)
file_obj.close()
