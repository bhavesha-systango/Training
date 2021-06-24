from class_and_object import Person

class Student(Person):
    def __init__(self, name, age, nationality, phone_no):
        self.phone_no=phone_no
        super().__init__(name, age, nationality)

    def get_phone_no(self):
        return self.phone_no

    def get_class(self):
        return self


s1 = Student("aryan",24,"indian",8878)
print(s1.get_phone_no())
print(s1.get_class())
print(s1.greet())
