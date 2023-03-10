t = int(input())

for i in range(t):
    n = int(input())
    text = input()
    error = 0
    step = 1
    while(len(text)>1):
        if step:
            if text[0]==text[1]:
                if (len(text)>2) and text[0]!=text[2]:
                    print("NO")
                    error = 1
                    break
            text = text[1:]
            step = 0
        else:
            if text[0]!=text[1]:
                print("NO")
                error = 1
                break
            text = text[2:]
            step = 1
    if not step and not error:
        print("NO")
        continue
    if error == 0:
        print("YES")
