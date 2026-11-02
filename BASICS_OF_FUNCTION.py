 # Program: Sum and Subtraction Functions

# Function to calculate sum of two numbers
def add(a, b):
    return a + b

# Function to calculate subtraction of two numbers
def subtract(a, b):
    print(f"Subtraction of {a} and {b}:",a - b)
    
def multiply(a,b=5):
    return(a*b)

# Calling functions multiple times
result=add(10, 5)
print("Sum of 10 and 5:", result)

subtract(10, 5)

print("multiply of 20 and 15:", multiply(20, 15))

print("multiply of 20 and default value:", multiply(20))

print("Sum of 100 and 50:", add(100, 50))

