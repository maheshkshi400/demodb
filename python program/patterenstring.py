string =input("Enter the string: ")
length= lenp(string)

for row in range(length):
    for col in range(row+1):
        print(string[col],end="")
    
    print()
