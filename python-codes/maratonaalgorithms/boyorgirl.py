input = input()
writtedletters = []
for item in input:
    if item not in writtedletters:
        writtedletters.append(item)
#print(writtedletters)
if(len(writtedletters)%2==0):
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")