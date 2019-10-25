n=int(input("Enter number:"))
m=str(n)
if(m==m[::-1]):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")