string1 = input()
string2 = input()
meaning = 0
count = 0
reversecount = len(string1)
if len(string1) == len(string2):
    while reversecount > 0:
        if string1[count] != string2[reversecount-1]:
            meaning = 1
        reversecount -= 1
        count += 1
    if meaning == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
