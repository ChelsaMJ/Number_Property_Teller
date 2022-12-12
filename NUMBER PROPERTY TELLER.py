# PROJECT : NUMBER PROPERTY TELLER
# Take an integer input from user and print the following info abt it: 
# 1,odd/even 
# 2,prime/composite 
# 3,palindrome/not 
# 4,no. of factors 
# 5,sum of all natural numbers till that number 
# 6,factorial of that number 
# 7,all fibonacci numbers till that number

#---------------------------------CODE----------------------------------

n=int(input("Enter any integer: "))  
print("The number you have entered is:",n)
print("Some of the properties of the number",n,"are:")

def EvenOrOdd(n):
    if n%2==0:
        print(n,"is an EVEN number")
    else:
        print(n,"is an ODD number")

def PrimeOrComposite(n):
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                print(n,"is a composite number, because",end=" ")
                print(i,"times",n//i,"is",n)
                break
        else:
            print(n,"is a prime number")
    else:
        print(n,"is neither prime nor composite")

def PalindromeOrNot(n):
    reverse_n=" "
    for i in str(n):
        reverse_n=i+reverse_n
        print('the reverse of the number is:',reverse_n)
    if str(n)==reverse_n:
        print('Yes, the number',n,'is a palindrome number.')
    else:
        print('No, the number',n,'is not a palindrome number.')
    
def Factors(n):
    c=0
    print("The factors of",n,"are:")
    for i in range(1, n + 1):
        if n % i == 0:
            c=c+1
    l=[]
    for i in range(1,n+1):
        if n%i==0:
            l.append(i)
    print(l)
    print("the number of factors are:",c)

def Sum(n):
    s=0
    for i in range (0,n):
        s+=i
    print("The sum of the natural numbers till",n,"is",s)

def Factorial(n):
    fact = 1
    if n < 0:
        print("factorial does not exist for negative numbers")
    elif n == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,n + 1):
            fact = fact*i
        print("The factorial of",n,"is",fact)

def FibonacciSeries(n):
    n1, n2 = 0, 1
    count = 0
    if n <= 0:
        print("Please enter a positive integer")
    elif n == 1:
        print("Fibonacci series upto",n,":")
        print(n1)
    else:
        print("The Fibonacci series till",n,"is:")
    while count < n:
        print(n1, end=",")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1