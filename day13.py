# Day 15 - Thermal Physics Calculator for Civil Engineers

print("🔥 THERMAL STRESS CALCULATOR - Day 15 🔥\n")

# --- Part 1: Bimetallic Strip & Expansion Joint Calculator ---
L0 = float(input("Enter Length of Rail/Bridge in meters: "))
alpha = 12e-6  # for steel
T1 = float(input("Enter Winter Temp (C): "))
T2 = float(input("Enter Summer Temp (C): "))

delta_T = T2 - T1
delta_L = L0 * alpha * delta_T

print(f"\nTemperature Difference: {delta_T} C")
print(f"Expansion in Length: {delta_L*1000:.2f} mm")
print(f"So you need an Expansion Gap of at least {delta_L*1000:.2f} mm")

# --- Part 2: Thermal Stress if expansion is blocked ---
Y = 200e9  # Young's modulus for steel in Pa
stress = Y * alpha * delta_T
print(f"\nIf expansion is BLOCKED, Thermal Stress = {stress/1e6:.2f} MPa")
print("This stress is enough to BEND the track! (Buckling)")

# --- Part 3: Bimetallic Strip Bending ---
print("\n--- Bimetallic Strip ---")
alpha_brass = 19e-6
alpha_invar = 1.2e-6
diff_alpha = alpha_brass - alpha_invar
print(f"Bending is proportional to (alpha_brass -
