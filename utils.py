# prime number

# nums=int(input("Enter a number:"))
# is_prime=True

# if nums>1:
#     for i in range(2,nums):
#         if(nums%i==0):
#             is_prime=False
#             break
#         if is_prime:
#             print("the number is prime")
#         else:
#             print("the number is not a prime")
            
            
# fibonacci series

# nums=int(input("enter a number:"))

# prev=0
# next=1
# sum=0

# for i in range(nums):
#     print(sum)            
#     prev=next
#     next=sum
#     sum=prev+next
    
    
#  reverse a number

# nums=int(input("enter a number:"))

# reverse=0

# while nums>0:
#     digit=nums%10
#     reverse=reverse*10+digit
#     nums//=10
# print("the reverse of the number is :",reverse)


# Pallindrome number

# nums=int(input("enter a number to check it is pallindorme or not:"))

# temp=nums
# reverse=0
# while temp>0:
#     digit=temp%10
#     reverse=reverse*10+digit
#     temp//=10
# if nums==reverse:
#     print("number is a pallindrome number ")
# else:
#      print("number is not a pallindrome number")
     
     
#Factorial of a number

# nums=int(input("enter a number to find the factorial of the number:"))
# fact=1

# for i in range(1,nums+1):
#     fact=fact*i
# print("factorial of the number is:",fact)


print("1. Prime Number")
print("2. Fibonacci Series")
print("3. Reverse a Number")
print("4. Palindrome Number")
print("5. Factorial of a Number")
nums=int(input("enter a option to run the program: "))

# Prime Number
if nums==1:
     print("you are checking for a prime number")
     num=int(input("enter a number to check it is prime or not:"))
     is_prime=True
     if num>1:
      for i in range(2,num):
        if(num%i==0):
            is_prime=False
            break
        if is_prime:
             print("the number is prime")
        else:
             print("the number is not a prime")
# Fibonacci Number
if nums==2:
     num2=int(input("enter number to print fibonacci number"))
    
     prev=0
     next=1
     sum=0
     for i in range(num2):
         print(sum)
         prev=next
         next=sum
         sum=prev+next
# fibo(num2=5)
    
if nums==3:
     #reverse a number

    num3=int(input("enter a number to  get reverse  of it:"))

    reverse=0

    while num3>0:
        digit=num3%10
        reverse=reverse*10+digit
        num3//=10
    print("the reverse of the number is :",reverse)

if nums==4:
    
# Pallindrome number

    num4=int(input("enter a number to check it is pallindorme or not:"))

    temp=num4
    reverse=0
    while temp>0:
        digit=temp%10
        reverse=reverse*10+digit
        temp//=10
    if num4==reverse:
        print("number is a pallindrome number ")
    else:
        print("number is not a pallindrome number")
     
if nums==5:
    #Factorial of a number

    num5=int(input("enter a number to find the factorial of the number:"))
    fact=1

    for i in range(1,num5+1):
        fact=fact*i
    print("factorial of the number is:",fact)    

        
        

    
        
        
