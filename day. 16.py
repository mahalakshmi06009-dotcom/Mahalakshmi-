# Day 16 - Civil Engineer Python - Smart Estimation Tool
# Topic: Quantity Surveying & Material Calculator

print("🏗️ DAY 16 - SMART ESTIMATION & COSTING TOOL 🏗️\n")

# Input from Site Engineer
length = float(input("Enter Room Length (m): "))
breadth = float(input("Enter Room Breadth (m): "))
thickness = float(input("Enter Slab Thickness (m) - eg 0.15: "))

# --- 1. Quantity Calculation ---
volume_concrete = length * breadth * thickness
print(f"\nConcrete Volume Required = {volume_concrete:.2f} m3")

# M20 Mix Ratio 1:1.5:3
cement_bags = (volume_concrete * 1 * 320) / 1 # 1m3 = 6.4 bags approx for M20
sand_tonne = volume_concrete * 0.42 * 1.6 # m3 to tonne
aggregate_tonne = volume_concrete * 0.84 * 1.5

print(f"Cement Required = {volume_concrete * 6.4:.1f} Bags")
print(f"Sand Required = {sand_tonne:.2f} Tonne")
print(f"Aggregate Required = {aggregate_tonne:.2f} Tonne")

# --- 2. Steel Calculation ---
steel_percentage = 80 # kg per m3 for slab
steel_kg = volume_concrete * steel_percentage
print(f"Steel Required = {steel_kg:.0f} kg ({steel_kg/1000:.2f} Tonne)")

# --- 3. Cost Estimation (Tiruppuvanam 2026 Rate) ---
cement_rate = 420 # per bag
sand_rate = 2500 # per tonne
aggregate_rate = 1800 # per tonne
steel_rate = 65 # per kg

total_cost = (volume_concrete * 6.4 * cement_rate) + (sand_tonne * sand_rate) + (aggregate_tonne * aggregate_rate) + (steel_kg * steel_rate)

print(f"\n--- COST ESTIMATION ---")
print(f"Cement Cost: Rs. {volume_concrete * 6.4 * cement_rate:.0f}")
print(f"Sand Cost: Rs. {sand_tonne * sand_rate:.0f}")
print(f"Total Slab Cost = Rs. {total_cost:.0f}")

# --- 4. Labour Cost ---
labour_cost = total_cost * 0.30
grand_total = total_cost + labour_cost
print(f"Labour (30%) = Rs. {labour_cost:.0f}")
print(f"\n💰 GRAND TOTAL = Rs. {grand_total:.0f}")

print("\n✅ One Click Estimation - No more Excel Sheets!")
