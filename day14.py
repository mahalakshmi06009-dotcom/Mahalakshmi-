# Day 14 - Civil Engineer Python - Environmental Calculator
# Subject: Wastewater + Solid Waste (Your Q14 Assignment)

print("🌊 DAY 14 - ENVIRONMENTAL ENGINEERING CALCULATOR 🌊\n")

# --- PART 1: Wastewater Treatment Plant Design ---
print("--- 1. SEWAGE QUANTITY & BOD CALCULATION ---")
population = int(input("Enter Population of area: "))
water_supply = 135  # LPCD as per IS

sewage_qty = population * water_supply * 0.8 / 1000000  # in MLD
print(f"Total Sewage Generated = {sewage_qty:.2f} MLD")

bod_per_person = 45
