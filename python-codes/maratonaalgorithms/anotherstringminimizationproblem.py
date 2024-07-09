t=int(input())
for i in range(t):
    n,m=map(int,input().split()) 
    l=[eval(i) for i in input().split()]
    s=["B" for i in range(m)]
    for i in range(len(l)):
        if l[i]<(m+1-l[i]) and s[l[i]-1]!="A":
            s[l[i]-1]="A"
            #s.replace(s[l[i]-1],"A")
        elif l[i]>(m+1-l[i]) and s[m-l[i]]=="A":
            s[l[i]-1]="A"
            #s.replace(s[m+1-l[i]],"A")
        else:
            s[m-l[i]]="A"
    for i in s:
        print(i,end="")
    print("\n")
   
