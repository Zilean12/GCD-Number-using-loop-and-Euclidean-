# To Calculate  GCD of Two Numbers using While loop Method 
a = int(input("Enter 1st number: ")) # user input 
b = int(input("Enter 2nd number: "))# User input
C = 0 # to count the number of loop execute 
i = 1
while(i <= a and i <= b):
  if(a % i == 0 and b % i == 0):
    gcd = i
    C = C + 1

  i = i + 1

print("The GCD of", a, "and", b, "is", gcd)
print("Number of while loop execute :", C)
