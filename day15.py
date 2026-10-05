# Day 15 - Civil Engineer Python - Smart Traffic Signal (ITS)
# Subject: Transportation Engineering - Intelligent Transportation System

print("🚦 DAY 15 - ITS - SMART TRAFFIC SIGNAL CALCULATOR 🚦\n")

# --- ITS Adaptive Signal Control ---
print("Enter Vehicle Count from Sensors (Last 5 mins):")

north = int(input("North Side Vehicle Count: "))
south = int(input("South Side Vehicle Count: "))
east = int(input("East Side Vehicle Count: "))
west = int(input("West Side Vehicle Count: "))

total_vehicles = north + south + east + west
total_cycle_time = 120  # 2 mins total cycle in seconds

print(f"\nTotal Vehicles Detected: {total_vehicles}")

# Calculate Green Time proportionally (ITS Logic)
if total_vehicles == 0:
    print("No Traffic - All Signals RED (Power Saving Mode)")
else:
    north_green = (north / total_vehicles) * total_cycle_time
    south_green = (south / total_vehicles) * total_cycle_time
    east_green = (east / total_vehicles) * total_cycle_time
    west_green = (west / total_vehicles) * total_cycle_time

    print("\n--- SMART SIGNAL TIMING (Adaptive) ---")
    print(f"North Green Time: {north_green:.0f} sec")
    print(f"South Green Time: {south_green:.0f} sec")
    print(f"East Green Time: {east_green:.0f} sec")
    print(f"West Green Time: {west_green:.0f} sec")

    # --- ITS Logic - Congestion Alert ---
    max_lane = max(north, south, east, west)
    if max_lane > 50:
        print("\n🚨 ALERT: Heavy Congestion Detected!")
        print("Action: VMS Board -> 'Use Alternative Route' ")
        print("Action: Traffic Data Sent to TMC (Egmore Center)")
    
    # --- Fuel & Time Saved ---
    fuel_saved = total_vehicles * 0.02 # litres approx
    print(f"\nEstimated Fuel Saved vs Fixed Signal: {fuel_saved:.2f} Litres per cycle")

print("\n✅ This is how Chennai ITMS Project Works! (500 Junctions)")
