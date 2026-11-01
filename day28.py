# Sangam Age - Cities, Ports, Import & Export Program

def sangam_history():
    print("=== SANGAM AGE HISTORY ===")
    
    cities = {
        "Poompuhar": "Capital of Cholas",
        "Madurai": "Capital of Pandyas - City of Tamil Sangam",
        "Vanji / Karur": "Capital of Cheras",
        "Uraiyur": "Famous for Cotton Clothes",
        "Korkai": "Famous for Pearl"
    }

    ports = ["Muziris (Muchiri)", "Thondi", "Korkai", "Poompuhar", "Arikamedu"]

    exports = ["Black Pepper (Black Gold)", "Pearl", "Cotton Dresses", "Ivory", "Teak Wood", "Peacock Feather"]
    imports = ["Roman Gold Coins", "Wine (Yavana)", "Coral", "Arabian Horses", "Glass", "Copper"]

    print("\n1. IMPORTANT CITIES:")
    for city, info in cities.items():
        print(f" - {city}: {info}")

    print("\n2. IMPORTANT PORTS:")
    for port in ports:
        print(f" - {port}")

    print("\n3. EXPORT ITEMS (From Tamil Nadu):")
    for item in exports:
        print(f" - {item}")

    print("\n4. IMPORT ITEMS (To Tamil Nadu):")
    for item in imports:
        print(f" - {item}")

# Run Program
sangam_history()
print("\n--- Program Completed by Mahalakshmi - Civil Dept ---")
