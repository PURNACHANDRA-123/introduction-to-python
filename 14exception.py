x=input("enter a number1")
y=input("enter a number2")
try:
    z = x / int(y)
except ZeroDivisionError as e:
    print("exception occured is zero division error",e)
    
except TypeError as e:
    print("exception occured",type(e).__name__)
    z=None

print("division is",z)





















