length = 5 # feet
width = 4 # feet
height = 4 # feet

volume_cft = length * width * height
volume_litres = volume_cft * 28.31

print(f"Tank capacity = {volume_litres} litres")
if volume_litres > 1500:
    print("Big family ku enough!")
else:
    print("Small family ku ok!")
  
