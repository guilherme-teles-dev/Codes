cases = ""
while(cases != 0):
    cases = int(input())
    if cases != 0:
        exitplace = []
        comeplace = []
        relactiontype = ""
        for ilhas in range(cases):
            ilha = input().split(" -> ")
            exitplace.append(ilha[0])
            comeplace.append(ilha[1])
        c = 0
        while(c < len(exitplace) or relationtype == ""):
            if exitplace.count(exitplace[c]) > 1:
                relationtype = "Not a function."
            elif comeplace.count(comeplace[c]) > 1:
                relationtype = "Not invertible."
        if relationtype == "":
            relationtype = "Invertible"
        print(relation, ".")
