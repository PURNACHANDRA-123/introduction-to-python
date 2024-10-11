def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
r1=factorial(12)

print(r1)


def fibonaccisequence(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonaccisequence(n-1)+fibonaccisequence(n-2)
    
r2=fibonaccisequence(5)
print(r2)






# is this also applicable
# def fibonacci(n):
#   if n <= 1:  # Base cases: 0th and 1st Fibonacci numbers are 0 and 1
#     return n
#   else:
#     return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive step

# # Get input from the user
# nterms = int(input("Enter the number of terms: "))

# # Print the Fibonacci sequence
# print("Fibonacci sequence:")
# for i in range(nterms):
#   print(fibonacci(i))


