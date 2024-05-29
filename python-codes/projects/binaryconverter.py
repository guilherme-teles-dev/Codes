from math import pow
number = input("Digite número que deseja converter: ")
mode = input("Digite o modo que deseja operar[bin/hex/dec]: ")
hex = ""
bin = ""
dec = 0
hextable = [[[["0", "1"], ["2", "3"]], [["4", "5"], ["6", "7"]]], [[["8", "9"], ["A", "B"]], [["C", "D"], ["E", "F"]]]]
if(mode == "bin"):
    bin = number
    count = 8
    hex = str(hextable[int(bin[0])][int(bin[1])][int(bin[2])][int(bin[3])])+str(hextable[int(bin[4])][int(bin[5])][int(bin[6])][int(bin[7])])
    for c in bin:
        if c == "1":
           dec += int(pow(2, count))
        count -= 1
        
    print(hex)
    print(dec)
elif(mode == "hex"):
    hex = number
    print(bin)
    print(dec)
else:
    dec = number
    print(hex)
    print(bin)