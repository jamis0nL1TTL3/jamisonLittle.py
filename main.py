#Function 1
# Returns Area of Rectangle
def rect_area(width, length):
    return width * length
#Function 2
# Returns Surface Area of Rectangular Solid
def rect_surface_area(width, height, length):
    #2 × base_area + lateral_area
    return 2*(width*height + length*height)

# Request the dimension of a solid rectangular object

length = int(input("Enter the length of the the object as a integer: "))
width = int(input("Enter the width of the the object as a integer: "))
height = int(input("Enter the height of the the object as a integer: "))

print("Length = ", length, "Width = ", width, "Height = ", height)
print("Total Surface Area = ", str(rect_surface_area(length, width, height)))
print("Area of the rectangle: " + str(rect_area(length, width)))
