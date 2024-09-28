import argparse

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--num1",help="first number")
    parser.add_argument("--num2",help="second number")
    parser.add_argument("--operation",help="operation",\
                        choices=["add","sub","mul"]) #prevents from divison

    args=parser.parse_args()
    

    print(args.num1)
    print(args.num2)
    print(args.operation)

n1=int(args.num1)
n2=int(args.num2)
if args.operation=="add":
    print(n1+n2)
elif args.operation=="sub":
    print(n1-n2)
elif args.operation=="mul":
    print(n1*n2)
elif args.operation=="div":
    print(n1/n2)
else:
    print("invalid operation")



# Positional arguments must be provided and are identified by their position in the command.
# Optional arguments can be provided with prefixes and are not mandatory. They allow for more flexible input without breaking the program if not supplied.






