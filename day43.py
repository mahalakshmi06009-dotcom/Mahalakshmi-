# ===== PYTHON MASTER FILE =====

# 1. PRINT & INPUT
print("Vanakkam da Mapla!")
name = input("Name: ")

# 2. DATA TYPES
age = 21          # int
price = 99.5      # float
is_pass = True    # bool

# 3. CONDITION
if age >= 18:
    print("Major da")
else:
    print("Minor")

# 4. LOOP
for i in range(5):
    print(f"Count {i}")

# 5. LIST, TUPLE, SET, DICT
my_list = [1,2,3]
my_dict = {"name":"Mech","year":3}
print(my_dict["name"])

# 6. FUNCTION - Most Important
def area_circle(r):
    return 3.14 * r * r

print(area_circle(5))

# 7. FILE HANDLING (Project ku)
# with open("data.txt", "w") as f:
#     f.write("Hello Python")

# 8. FINAL MINI APP - Student Mark
marks = 
