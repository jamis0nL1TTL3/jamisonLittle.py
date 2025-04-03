# area of a rectangle using users input

def rect_area():
    '''Gets User input and uses given integers to calculate area of a rectangle

    Parameters:
    -----------
    width: int
        User inputs given width for the rectangle
    length: int
        User inputs given length for the rectangle

    Returns:
    --------
    Multiplies the two given integers and prints out the result
    '''
    width = int(input("Please enter an integer for the rectangle width: "))
    length = int(input("Please enter an integer for the rectangle length: "))
    return width * length
print(rect_area())
