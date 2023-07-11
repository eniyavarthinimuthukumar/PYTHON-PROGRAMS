def str(string1, string2, m, n):
    
    if m == 0:
        return True
    if n == 0:
        return False
 
    
    if string1[m-1] == string2[n-1]:
        return str(string1, string2, m-1, n-1)
 
    
    return str(string1, string2, m-1, n)
 
 

string1 = input("Enter the first string")
string2 = input("Enter the second string")
 
if str(string1, string2, len(string1), len(string2)):
    print("Yes")
else:
    print("No")

