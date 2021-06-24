class Person:
    def __init__(self,name,age,nationality):
        self.name=name
        self.age=age
        self.nationality=nationality

    def greet(self):
        return ("welcome", self.name)

    def get_my_age(self):
        return ("your age is", self.age)

    def eligible_for_vote(self):
        if(self.age>18):
            return True
        else:
            return False

    
p1 = Person("bhavesh", 22, "indian")
print(p1.greet())
print(p1.get_my_age())
print(p1.eligible_for_vote())