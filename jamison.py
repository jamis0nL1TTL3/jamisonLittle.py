# Make a function titled ‘rect_area’ that finds the area of a rectangle
# Make a function titled ‘rect_surface_area’ that calls ‘rect_area’ to find the surface area of a rectangle
# Ensure to print length, width, and height along with the total surface area at the end

def rect_area(length:int, width:int) -> int:
    '''Multiplies length and width of a rectangle to find area

    Parameters:
    -----------
    length: int
        First number provided is the length of rectangle
    width: int
        Second number provided is the width of rectangle

    Returns:
    --------
    Multiplies the two integers to find the area of the rectangle
    '''
    return length * width