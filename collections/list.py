a=["jeni","rithi",22,33]
b=[50,20,10,40,40]
print("first list:",a)
print("second list:",b)
print("1.append \n2.insert \n3.extend \n4.remove \n5.pop \n6.reverse \n7.length \n8.maximum \n9.minimum \n10.count no.of.occurance \n11.sort \n12.fetch \n13.concatenation \n14.repeat \n15.clear")
n=int(input("enter a number:"))
if(n==1):
  a.append("sandy")
  print(a)
elif(n==2):
  a.insert(4,44)
  print(a)
elif(n==3):
  a.extend(["allie",6])
  print(a)
elif(n==4):
  a.remove("jeni")
  print(a)
elif(n==5):
  a.pop(1)
  print(a)
elif(n==6):
  a.reverse()
  print(a)
elif(n==7):
  print("length of a:",len(a))
elif(n==8):
  print("maixmum of b:",max(b))
elif(n==9):
  print("minimum of b:",min(b))
elif(n==10):
  print("occurance of 40:",b.count(40))
elif(n==11):
  print(b.sort())
  print(b)
elif(n==12):
  print(b.index(10))
elif(n==13):
  print("cocatenating two list:")
  print(a+b)
elif(n==14):
  print("repeating b:")
  print(b*2)
elif(n==15):
  print("clearing b:")
  b.clear()
  print(b)
else:
  print("input value is not valid,choose 1 to 15:")
