class Car:
    def __init__(self,name,color,model,energy):
        self.name = name
        self.color =color
        self.model = model
        self.energy = energy

    def goBack(self):
        print(self.name,'is going Back')

    def goForward(self):
        print(self.name,'is going forward')

if __name__ == '__main__':
    car1 = Car("Kia","red","2018","Benzene")
    car2 = Car("BMW","Green","2008","Benzene")

    car1.goBack()
    car2.goForward()
