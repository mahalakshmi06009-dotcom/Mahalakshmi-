print("--- Number Series Generator ---")
n = int(input("Enter number of terms: "))

print("\n1. Arithmetic")
print("2. Geometric") 
print("3. Fibonacci")
choice = int(input("Enter your choice: "))

if choice == 1:
    a = int(input("Enter first term: "))
    d = int(input("Enter common difference: "))
    print("Arithmetic Series: ", end="")
    for i in range(n):
        print(a + i*d, end=" ")

elif choice == 2:
    a = int(input("Enter first term: "))
    r = int(input("Enter common ratio: "))
    print("Geometric Series: ", end="")
    term = a
    for i in range(n):
        print(term, end=" ")
        term *= r

elif choice == 3:
    a, b = 0, 1
    print("Fibonacci Series: ", end="")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a+b

else:
    print("Invalid Choice")
