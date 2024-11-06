def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage:
print(fibonacci(10))  # Output: 55 # this tells what is the value of 10th position in fibonacci series not sum