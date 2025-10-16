n = int(input("Enter no of rows:"))

for row in range(1,n+1):
    dummy = row
    for col in range(1,n+1):
        print(dummy,end='')
        if row%2 == 1:
            dummy += 1
        else:
            dummy += 2
    print()