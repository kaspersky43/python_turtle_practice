h = int(input())
k = int((h-1)/2)
base = h + 2*k 

for i in range(h):
    for c in range(base):
        if(c in range(h-i-1,h+i)):
            print('*',end='')
        else:
            print(' ',end='')
    print()
