def is_prime(num):
    
    if num<=1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True

def fibonacci(n):
    a,b=0,1
    for i in range(n):
        print(a)
        a,b=b,a+b
        
def reverse_number(num):
    rev=0
    while num>0:
        digit=num%10
        rev=rev*10+digit
        num//=10
    return rev

def is_palindrome(num):
    return num==reverse_number(num)

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact

# Main Program

print("1. check if the  number is prime")
print("2. genretae fibonacci series")
print("3. reverse a number")
print("4. check if the number is palindrome")
print("5. find the factorial of a number")

choice=int(input("Enter your choice:"))

if choice==1:
    num=int(input("Entner a number to check if it is prime r not"))
    print("Prime" if is_prime(num) else "Not Prime")
elif choice==2:
    n=int(input("enter the number of terms for fibonaccii series"))
    fibonacci(n)
elif choice==3:
    num=int(input("enter a number to reverse"))
    print("reverse number is:",reverse_number(num))
elif choice==4:
    num=int(input("enter a number to check if it is palindrome or not"))
    print("palindrome" if is_palindrome(num) else "not a plaindrome")
elif choice ==5:
    num=int(input("enter a number to find the factorial"))
    print("factorial of the number is",factorial(num))
else:
    print("invalid choice")
    