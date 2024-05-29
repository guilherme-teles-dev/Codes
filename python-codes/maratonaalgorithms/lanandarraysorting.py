for c in range(int(input())):
    elements = [int(input())]
    elements = list(map(int, input().split()))
    if len(elements)%2!=0 or elements == sorted(elements) or len(elements)==1:
        print("YES")
    else:
        print("NO")
