def calculate_total_cost(area):
    # Complex logic hidden from user
    base_cost = area * 1200
    gst = base_cost * 0.18
    final_cost = base_cost + gst
    return final_cost

# User side - Very Simple
# User doesn't know about GST calculation
print(calculate_total_cost(1000)) # Output: 1416000
