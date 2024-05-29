l = []
finish = True
while finish:
    try: #say to python to try append an input in l
        l.append(input())
        
    except EOFError: #if it's not possible input, means an empty input and can finally end the code.
        finish = False
        
l = set(l) #this function is used to remove duplicates in array, very useful in this case to count the different inputs.
print(len(l))
