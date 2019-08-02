class Student:
    def __init__(self,first_name,last_name,std_id):
        self.first_name = first_name
        self.last_name = last_name
        self.std_id = std_id
        self.email = first_name + '.' + last_name + '@university.com'

    def getFullName(self):
        return self.first_name + ' ' + self.last_name

    def getEmail(self):
        return self.email

if __name__ == '__main__':
    student1 = Student("Fatima","sam",2008)
    print('The Full Name is ',student1.getFullName(),"\nThe email is ",student1.getEmail())
    print('---------------------------------------------')
    student2 = Student("Basmah","Hamdan",2012)
    print('The Full Name is ',student2.getFullName(),"\nThe email is ",student2.getEmail())
    print('---------------------------------------------')
    student3 = Student("Wejdan","Althobiti",2014)
    print('The Full Name is ',student3.getFullName(),"\nThe email is ",student3.getEmail())
    print('---------------------------------------------')

