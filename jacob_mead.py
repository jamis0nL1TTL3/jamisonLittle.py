def rect_surface_area(length: int, width: int, height: int) -> int:
    return 2 * (rect_area(length, width) + rect_area(length, height) + rect_area(width, height))
if __name__ == "__main__":
    l = int(input("Length?\n>>"))
    w = int(input("Width?\n>>"))
    h = int(input("Height?\n>>"))
    print(rect_surface_area(l, w, h))
