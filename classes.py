class Car:
    color = ""
    name = ""
    model = 0
    energy = ""

    def goBack(self):
        print(self.name,'Car is going back')

    def goForward(self):
        print(self.name,'Car is going forward')




if __name__ == '__main__':
    car1 = Car()
    car1.color = "red"
    car1.name = "Kia"
    car1.model = 2018
    car1.energy = "Benzene"
    car1.goForward()

    car1 = Car()
    car1.color = "Green"
    car1.name = "BMW"
    car1.model = 1990
    car1.goBack()
