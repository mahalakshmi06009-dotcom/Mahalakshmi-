# Day 11 - UK Dream Salary Calculator

print("🇬🇧 UK Civil Engineer Salary Calculator 🇬🇧")

# UK la per hour salary
hourly_rate = float(input("Per Hour Rate in Pound (£) : "))
hours_per_week = int(input("Per Week Hours : "))

weekly_salary = hourly_rate * hours_per_week
monthly_salary = weekly_salary * 4
yearly_salary = weekly_salary * 52

# Indian Rupee ku convert - 1 Pound = 110 Rs
inr_rate = 110
yearly_inr = yearly_salary * inr_rate

print("\n--- YOUR UK SALARY ---")
print(f"Weekly Salary: £{weekly_salary}")
print(f"Monthly Salary: £{monthly_salary}")
print(f"Yearly Salary: £{yearly_salary}")
print(f"Yearly in Indian Rupees: Rs {yearly_inr:,.0f}")

if yearly_salary > 30000:
    print("\n🎉 You are eligible for UK Skilled Worker Visa!")
else:
    print("\n💪 Try to upskill more - Target £35
