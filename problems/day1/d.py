t = int(input())

for i in range(t):
    c1,c2,c3 = map(int, input().split())  
    a1,a2,a3,a4,a5 = map(int, input().split())
    
    c1 -= a1
    c2 -= a2
    c3 -= a3

    if (c1<0 or c2<0 or c3<0):
        print("NO")
        continue

    if c1+c3<a4:
        print("NO")
        continue
    
    c1-= a4
    if c1<0:
        c3+=c1

    if c2+c3<a5:
        print("NO")
        continue
    
    print("YES")