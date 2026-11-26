expenses = []
while True:
    amt = input("Amount (or 'q' to quit): ")
    if amt == 'q': break
    expenses.append(int(amt))

print(f"Total: {sum(expenses)}")
