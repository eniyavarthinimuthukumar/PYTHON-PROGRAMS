c={}
n=int(input ("enter the number of elements:")) 
for i in range(n) :
    key=input("Enter the key") 
    value=input("Enter the value") 
    c[key]=value
for key, value in c.items():
  print(key,value)
