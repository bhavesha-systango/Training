from class_and_object import Person

class Student(Person):
    def __init__(self, phone_no):
        self.phone_no=phone_no

    def get_phone_no(self):
        return self.phone_no

    def get_class(self):
        return self


s1 = Student(8878385967)
print(s1.get_phone_no())
print(s1.get_class())
