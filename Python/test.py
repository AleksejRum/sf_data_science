# Calculate the factorial by recursion
def get_factorial(n):
    if n == 1:
        return n
    return n*(get_factorial(n-1))
    
print(get_factorial(5))

# Calculate the factorial by cycle
def get_factorial2(n):
    factorial = 1
    for i in range(1,n+1):
        factorial *= i
    return factorial

print(get_factorial2(5))   