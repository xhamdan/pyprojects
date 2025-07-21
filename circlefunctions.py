#Compute-Area(2TTr2-SA-Circumference2TTr.Diameter(2r)

def compute_diameter(radius):
    diameter = 2 * radius

    return diameter

def compute_area(radius): #We parse radius as a param bcz its unknown and changes from circle to circle
    area = 3.14 * radius **2

    return area 


#compute diameter here while provided the radius
radius = float(input("Enter value of the Radius: "))
print(f" The diameter is: {compute_diameter(radius)} ")
