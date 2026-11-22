""" Q. Write a program to take input for the length and the height of a rectangle. 
Calculate and print the perimeter and area of the rectangle. """

length = float(input("Length: "))
width = float(input("Width: "))

perimeter = (length + width) * 2
area = length * width
print(f"Perimeter = {perimeter} Area = {area}")