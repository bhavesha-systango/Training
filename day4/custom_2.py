class Error(Exception):
    pass


class custom_222(Error):
    def __init__(self, prev, nxt, msg):
        self.prev = prev
        self.nxt = nxt
        self.msg = msg

    def print_rrr(self):
        return(self.prev, self.nxt, self.msg)


try:
    raise custom_222(2, 3, "take the exception")
except custom_222 as cus:
    print("the exception is", cus.prev, cus.nxt, cus.msg)