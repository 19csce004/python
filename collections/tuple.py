a=('english',91,'tamil',90.5)
b=(11,33,100,88,4)
c=("Pythonprogramming")
d=("Python","Cloudcomputing","linux")
print("TUPLE ONE:",a)
print("TUPLE TWO:",b)
print("TUPLE THREE:",c)
print("TUPLE FOUR:",d)
n=int(input("enter your choice:"))

if(n==1):
    print("Datatype of tuple one is:",type(a))
    print("Datatype of tuple two is:",type(b))
elif(n==2):
    print("Length of tuple one:",len(a))
    print("Length of tuple two:",len(b))
elif(n==3):
    r=int(input("enter the no.of times to be repeat:"))
    print("Repeatation of tuple one:",a*r)
    print("Repeatation of tuple two:",b*r)
elif(n==4):
    i=int(input("enter the index number you want:"))
    print("element in the index value",i,"is :",a[i])
    print("element in the index value",i,"is :",b[i])
elif(n==5):
    e,b,c,d=a
    print(e)
    print(b)
    print(c)
    print(d)
elif(n==6):
    f=a+b
    print(f)
elif(n==7):
    print(c)
    rem=int(input("enter the places want to remove from first:"))
    print(c[rem:])
elif(n==8):
    print(c)
    rem=int(input("enter the place you want to remove from last:"))
    print(c[:-rem])
elif(n==9):
    print(c)
    print(c[::-1])
elif(n==10):
    print(c)
    e1=int(input("enter the starting range:"))
    e2=int(input("enter the ending range:"))
    print(c[e1:e2])
elif(n==11):
    print(t5)
    i1=int(input("enter the index value :"))
    e1=int(input("enter the starting range:"))
    e2=int(input("enter the ending range:"))
    print(t5[i1][e1:e2])
elif(n==12):
    d=str(input("enter the tuple you want to delete (t1/t2/t4/t5): "))
    del(d)
elif(n==13):
    print(t2)
    print("Maximum of tuple two is :",max(t2))
elif(n==14):
    print(t2)
    print("Minimum of tuple two is :",min(t2))
elif(n==15):
    print(t2)
    print("Sum of the tuple two is :",sum(t2))
elif(n==16):
    print(t2)
    print("Sorting the tuple two :",sorted(t2))
elif(n==17):
    print(t2)
    print("Reverse sorting the tuple two:",sorted(t2,reverse=True))
elif(n==18):
    n="Python is a open source language"
    print(n)
    print("DataType before :",type(n))
    t3=tuple(n)
    print("DataType after changing :",type(t3))
elif(n==19):
    n="Python is a open source language"
    i=int(input("enter an index value:"))
    print("displaying an element of the index by reversing :",n[-i])
    print("Removing the indices by reversing :",n[:-i])
    print("reversing and also removing the particular index from tuple :",n[::-i])
else:
    print("invalid input!")
	
