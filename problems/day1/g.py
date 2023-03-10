t = int(input())

for i in range(t):
    n,a,b = map(int, input().split())
    if n == 0:
        print(0)
    if a>b:
        print(1)
    if b>=a:
        if n%a == 0:
            print(int(n//a))
        else:
            print(int(n//a)+1)