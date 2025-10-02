#Number of rows
n=int(input('Enter no of rows: '))
stars=1

#outer loop runs 'n' times
for row in range(1,n+1):

    #inner loop print stars
    for st in range(1,stars+1):
        print('*',end='')
    #print the next line
    print()

    #row '<=' increment the star or else decrement the star
    if row <= n//2:
        stars+=1
    else:
        stars-=1
