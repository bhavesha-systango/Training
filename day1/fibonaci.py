#fibonaaci series
a=0
b=1
n=int(input("enter no."))
for i in range(n):
        c=a+b
        a=b
        b=c
        print(c)
        