def checkDataType(input_value):
    "this function evulates the data type of the inputed value and prints message to the screen"
    datatype = type(input_value)
    print("you entered",input_value,"and the data type is",datatype)
    return True

checkDataType("James")
