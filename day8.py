# Today's Coding - Sep 28 - Billing System

print("🏗️ JK Hardware - Bill Generator 🏗️")

cement_price = 450  # per bag
sand_price = 60     # per cft
brick_price = 9     # per brick

c = int(input("Cement bags enna? : "))
s = int(input("Sand cft enna? : "))
b = int(input("Bricks enna? : "))

total = (c * cement_price) + (s * sand_price) + (b * brick_price)
gst = total * 0.18
grand_total = total + gst

print("\n--- BILL ---")
print(f"Cement {c} bags = Rs
