string = input()
string_lower = string.lower()
final_string = []
vowels = ["a", "e", "i", "o", "u", "y"]
for c in string_lower:
    if c not in vowels:
        print(".", end=c)