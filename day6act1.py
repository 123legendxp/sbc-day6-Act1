word=int(input(":"))
temp=word
rev=0
while(word>0):
    dig=word%10
    rev=rev*10+dig
    word=word//10
if(temp==rev):
    print("palindrome!")
else:
    print("Not a palindrome!")