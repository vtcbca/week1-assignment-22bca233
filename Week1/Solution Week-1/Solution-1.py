#1.Write a Python script to enter an y number and check its prime or not
def primeornot(n):
    ans=True
    for i in range(2,n):
        if(n%2==0):
            ans=False
            break
    if(ans==True):
        print("Number is prime!!")
    else:
        print("Number is not prime!!")


num=int(input("Enter a number:"))
primeornot(num)
