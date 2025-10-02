#Number of rows
N=int(input('Enter no of rows: '))
stars=(2*N)-1
spaces=0

#Outer loop runs N times, for each row
for i in range(1,N+1):
    
    #Inner loop prints spaces
    for sp in range(1,spaces+1):
        print(' ',end='')
        
    #Inner loop prints Stars
    for st in range(1,stars+1):
        print('*',end='')
    print()
    
    #while increases row spaces increasing and stars decreasing
    spaces+=1
    stars-=2
    
