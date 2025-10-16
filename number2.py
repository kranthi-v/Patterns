n = int(input("Enter no of rows: "))

for row in range(1,n+1):
    dummy = 1
    for col in range(1,n+1):
        print(dummy,end='')
        dummy += 1
    print()