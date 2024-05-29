def decoder(latter, cifra):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    latterposition = alphabet.index(latter)
    if(latterposition + cifra > len(alphabet)):
        latterposition -= len(alphabet)
    return(alphabet[latterposition+cifra])
cases = int(input())
words = []
for c in range(cases):
    word = input()
    cifra = int(input())
    finalword = []
    for latter in word:
        finalword.append(decoder(latter, cifra))
    words.append(finalword)
for c in words:
    newword = ''.join(c)
    print(newword)