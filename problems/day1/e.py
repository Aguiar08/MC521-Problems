t = int(input())

for i in range(t):
    x = int(input())
    if x == 1:
        print(0)
    else:
        count2=0
        count3=0
        while(x%3==0):
            x = x/3
            count3+=1
        while(x%2==0):
            x = x/2
            count2+=1
        if x!=1:
            print(-1)
        elif count2 > count3:
            print(-1)
        elif (count2==0 and count3==0):
            print(-1)
        elif count2==count3:
            print(count2)
        else:
            print(2*count3-count2)