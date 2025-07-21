#Compute-Area(2TTr2-Circumference2TTr.Diameter(2r)

def compute_diameter(radius):
    diameter = 2 * radius

    return diameter

def compute_area(radius): #We parse radius as a param bcz its unknown and changes from circle to circle
    area = 3.14 * radius **2

    return area 

def compute_circumference(radius):
    circumference = 2 * 3.14 * radius

    return circumference


#compute diameter here while provided the radius
radius = float(input("Enter value of the Radius: ")) #Same value can be used to find dia,area
print(f" The diameter is: {compute_diameter(radius)} ")
print(f" The area of the circle is: {compute_area(radius)} ")
print(f" The Circumference of the circle is: {compute_circumference(radius)} ")
