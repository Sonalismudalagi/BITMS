class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Professor(Person):
    def is_professor(self,name,age):
        return f'{self.name} is a professor'
sir=Professor()
print(sir.is_professor("Sonali",20))

            