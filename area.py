def calculate_area(base, height):
    print("__name__: ",__name__)
    return 1/2*(base*height)

if __name__ == "__main__":
    print("I am in area.py")
    a=calculate_area(10, 20)
    print("area: ",a)



#it showing main bcoz it is in main folder
#when importing file in amother py file it will create pyccache folder


