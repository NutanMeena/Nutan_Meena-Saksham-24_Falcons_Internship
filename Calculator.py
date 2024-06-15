def add(S,T):

    print(S+T)

def sub(S,T):
    print(S-T)

def mul(S,T):

    print(S*T)

def div(S,T):

    print(S/T)


print("-------Mini Calculator----------")

print("1. Addition")

print("2. Substraction")

print("3. Multiplication")

print("4. Division")

S=int(input("Enter the first number:"))

T=int(input("Enter the second number:"))

ch=input("Enter your choice:")

if ch== "1":
    add(S,T) 

elif ch=="2":

    sub(S,T) 

elif ch=="3":

    mul(S,T)

elif ch=="4":

    div(S,T) 

else:

    print("Invalid Input")


# calculate Tabel:


A=int(input("Enter the number:"))

for i in range (1,11):

    print(A,'x',i,'=',A*i) 


#calculater Factorial:
 
def fact(n):
    if n<0:

        return 0 

    elif n==0 or n==1:

        return 1

    else:

        fact=1

        while(n>1):

            fact*=n

            n -=1
        return fact 

n=int(input("Enter the number:"))
print("Factorial of ",n,"is",fact(n))