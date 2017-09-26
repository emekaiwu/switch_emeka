def calArea():
    length=input("enter length:")
    breadth=input("enter breadth")
    #check values
    while not str.isdigit(length) and not str.isdigit(breadth):
        length = int("suit length")
        breadth = int("suit breadth")
        print("please enter a value")

    else:
        length = int(length)
        breadth = int(breadth)
        area = length * breadth
        print("The area of the suit is",area)
        return area
calArea()


