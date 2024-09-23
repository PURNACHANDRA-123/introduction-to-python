#here you need to understand what is global and local variable


def print_pattern(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end=" ")
        print("\n")

x=4
print_pattern(x)
#calculate for area of triangle
def calculate_area(dimension1,dimension2,shape="triangle"):
    '''
    :param dimension1: In case of triangle it is "base". For rectangle it is "length".
    :param dimension2: In case of triangle it is "height". For rectangle it is "width".
    :param shape: Either "triangle" or "rectangle"
    :return: Area of a shape
    '''
    if shape=="triangle":
        area=1/2*(dimension1*dimension2) # Triangle area is : 1/2(Base*Height)
    elif shape=="rectangle":
        area=dimension1*dimension2 # Rectangle area is: Length*Width
    else:
        print("Error: Input shape is neither triangle nor rectangle.")
        area=None # If user didn't supply "triangle" or "rectangle" as shape then return None
    return area


height=5
base=3
area=calculate_area(height,base,"triangle")
print(area)


lenght=5
width=3
area=calculate_area(lenght,width,"rectangle")
print(area) 


