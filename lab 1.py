n=int(input("Enter a number :"))
fact=1
count=0
temp=n
rev=0
if(n%2!=0):
      for i in range(1,n+1):
          fact=fact*i
      print("The factorial number =",fact)
      while(fact!=0):
        fact=fact//10
        count=count+1
      print("The total number of digits =",count)

elif(n%2==0):
    while(n>0):
        digits=n%10
        rev=rev*10+digits
        n=n//10
    if(rev==temp):
        print("Palindrome")
    else:
        print("Not a palindrome")

else:
    print("Invalid entry")
    
            
        
        
        
          
      
      
      
