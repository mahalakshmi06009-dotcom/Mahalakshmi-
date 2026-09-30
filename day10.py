# Day 12 - House Construction Cost Calculator

print("🏠 SMART HOUSE COST ESTIMATOR 🏠\n")

sqft = int(input("Veetu Area enna Sqft la? : "))
rate = int(input("Per Sqft Rate enna? (Ex: 1800) : "))

basic_cost = sqft * rate

# Extra charges
if sqft > 1500:
    print("\nBig House = Extra 5% for Elevation Design")
    basic_cost = basic_cost + (basic_cost * 0.05)

print("\n--- FINAL ESTIMATION ---")
print(f"Total Area: {sqft} Sqft")
print(f"Basic Cost: Rs {basic_cost:,.0f}")

# EMI option
months = int(input("\nEMI la kattanuma? Enna Months? (ex: 12) : "))
emi = basic_cost / months
print(f"Monthly EMI: Rs {emi:,.0f} per month")

print("\n🏗️ Budget Ready! Client kitta sollidalam!")
