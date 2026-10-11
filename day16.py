 a=int(input("Enter the starting number:"))
r=int(input("Enter the common ratio:"))
n=int(input("Enter the number of terms N:"))
term=a
print(term,end=" ")
for i in range(1,n):
    term=term*r
    print(term,end=" ")
