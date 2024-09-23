india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city=input("enter the city name")

if city in india:
    print("india")
elif city in pakistan:
    print("pakistan")
elif city in bangladesh:
    print("bangladesh")
else:
    print("unknown")


city1=input("enter the city 1 name")
city2=input("enter the city 2 name")

if city1 in india and city2 in india:
    print("india")
elif city1 in pakistan and city2 in pakistan:
    print("pakistan")
elif city1 in bangladesh and city2 in bangladesh:
    print("bangladesh")
else:
    print("may be from different country or not belonging to any country")





