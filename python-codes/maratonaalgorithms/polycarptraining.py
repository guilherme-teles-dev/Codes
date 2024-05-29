input() #can i leave the input alone? without put this in any variable?
r=0
for x in sorted(map(int, input().split())):r+=x>r #WFT is this? r recive x if it's bigger than r?
print(r)
