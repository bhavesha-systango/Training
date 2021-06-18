n=int(input("enter no."))
flag=0
for i in range(2,n):
        if(n%i==0):
                flag=1

if(flag==1):
        print("not a prime no.",n)
else:
        print("it is a prime no.",n)
        