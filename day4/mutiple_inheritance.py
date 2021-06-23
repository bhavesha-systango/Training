class A:
    def func1(self):
        print("this is 1 function", self.value)


class B:
    def func2(self):
        print("this is 2 function", self.value)


class C(A, B):
    def __init__(self, value):
        self.value = value


c1 = C(5)
c1.func1()
c1.func2()