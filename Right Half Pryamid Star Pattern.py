#number of rows
N=int(input('enter no of rows: '))

#Outer loop runs N times for each row
for i in range(1,N+1):
    
    #Inner loop print stars 'i' no of times
    for j in range(1,i+1):
        print('*',end='')
        
    #Move to the next line
    print()
