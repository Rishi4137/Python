class Person:
    def __init__(self,name):
        self.name=name;
    def talk(self):
        print("Hello I am "+self.name)


p1=Person("Rishi")
print(p1.name)
p1.talk()
