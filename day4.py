# UK style cost
area_sqft = float(input("House area in sqft: "))
rate_per_sqft = 1800 # Rs

total_cost = area_sqft * rate_per_sqft
print(f"Total cost = Rs {total_cost:,}")

# UK pounds ku convert
pounds = total_cost / 105 # 1 pound = 105 Rs approx
print(f"In UK Pounds = £{round(pounds, 2)}")
