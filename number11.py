n = int(input("Enter no of rows: "))
spaces = n-1
number = 1
for row in range(1,n+1):
    dummy = 1
    for sp in range(1,spaces+1):
        print(' ',end='')
    for num in range(1,number+1):
        print(dummy,end='')
        if num <= number//2:
            dummy+=1
        else:
            dummy-=1
    print()
    spaces -= 1
    number += 2