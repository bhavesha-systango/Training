class Error2(Exception):
    def __init__(self, prev, msg):
        self.prev = prev
        self.msg = msg


class Derived(Error2):
    def value6(self):
        print(self.msg+'is', self.prev)

    
d1 = Derived(6, "the value of x")
d1.value6()
        
