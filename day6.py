# All-in-One Civil Calculator - By Future UK Engineer 🇬🇧

def civil_calculator():
    print("--- Civil Engineer Calculator ---")
    print("1. Room Area")
    print("2. Brick Count")
    print("3. Concrete Volume")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        l = float(input("Length (ft): "))
        b = float(input("Breadth (ft): "))
        print(f"✅ Area = {l*b} sqft")

    elif choice == "2":
        area = float(input("Wall area (sqft): "))
        bricks = area / 0.66
        print(f"✅ Bricks needed = {int(bricks)}")

    elif choice == "3":
        l = float(input("Length (m): "))
        w = float(input("Width (m): "))
        t = float(input("Thickness (m): "))
        vol = l*w*t
        print(f"✅ Concrete = {vol} cum")
        print(f"✅ Cement bags = {vol*6.5:.1f} bags")

    else:
        print("Wrong choice da!")

    print("\nDream: UK 🇬🇧 | Keep coding!")

# Run it
civil_calculator()
