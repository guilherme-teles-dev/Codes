def lexcographweight(word):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    weight = 0
    for latter in word:
        location = alphabet.index(latter.upper())
        weight += location+1
    return weight
