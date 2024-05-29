#constructive algorithms
#math
#1000
numberofnumbers = int(input())
favority_integers = [numberofnumbers]
favority_integers = list(map(int, input().split()))
#processing
for c in favority_integers:
    favorite = False
    i = 20
    if c < 15:
        print("NO")
    else:
        while(i >= 15):
            if (c-i)%14==0:
                favorite = True
            i -= 1
        if favorite == False:
            print("NO")
        else:
            print("YES")
    
