def hcf(x,y):
        if x < y:
                smallest=x
        else:
                smallest=y
        while(True):
                if((x % smallest ==0)and(y%smallest==0)):
                        hcf=smallest
                        break
                smallest-=1
        return hcf

x=int(input("enter no."))
y=int(input("enter no."))
print("the hcf is",hcf(x,y))

