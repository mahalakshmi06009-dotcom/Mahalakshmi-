# Day 14 - Floor Tile Calculator

print("💎 TILE ESTIMATOR - Day 14 💎\n")

room_len = float(input("Room Length (feet): "))
room_wid = float(input("Room Width (feet): "))
tile_size = float(input("Tile Size (feet) - ex: 2 for 2x2: "))

room_area = room_len * room_wid
tile_area = tile_size * tile_size

tiles_needed = room_area / tile_area
total_with_wastage = tiles_needed * 1.15  # 15% wastage for cutting

print(f"\nRoom Area: {room_area} Sqft")
print(f"Tiles Needed: {total_with_wastage:.0f} Nos")

cost_per_tile = float(input("\nCost per Tile (Rs): "))
total_cost = total_with_wastage * cost_per_tile

print(f"Total Cost: Rs. {total_cost:.0f}")
print("\n✅ Client ku estimate kudukka ready!")
