class custom_exception(Exception):
    def __init__(self, value):
        self.value = value
    
    def print_rr(self):
        return (repr(self.value))


try:
    raise(custom_exception(3*2))
except custom_exception as e:
    print("an exception occured", e.value)
