# Quantity of Concrete for Slab
length = float(input("Length (m): "))
breadth = float(input("Breadth (m): "))
thickness = float(input("Thickness (m): "))

volume = length * breadth * thickness
print(f"Concrete Volume = {volume} m3")

# Cement bags needed (1 m3 = 6.5 bags approx)
bags = volume * 6.5
print(f"Cement Bags Needed = {bags:.2f}")
