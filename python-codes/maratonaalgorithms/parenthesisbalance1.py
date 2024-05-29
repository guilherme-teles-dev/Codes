while True:
    try:
        expressions = input()
        right = 0
        for latter in expressions:
            if latter == "(":
                right += 1
            elif latter == ")":
                right -= 1
                if right < 0:
                    break
        if right != 0:
            print("incorrect")
        else:
            print("correct")
    except EOFError:
        break