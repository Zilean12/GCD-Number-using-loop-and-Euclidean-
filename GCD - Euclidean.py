
# To Calculate  GCD of Two Numbers using Euclidean Method 

def gcd(a, b):
    count = 0 
    while b != 0:
        count += 1
        a, b = b, a % b
    return (a, count)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result, C = gcd(num1, num2)

print("The GCD of", num1, "and", num2, "is", result)
print("Number of Euclidean execute:", C)
