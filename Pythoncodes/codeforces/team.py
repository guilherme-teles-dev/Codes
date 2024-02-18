##Problem to verify if the girls can resolve to problemset##
problems = int(input()) #Here we are catching from user the number of problemsets
problemsfinished = 0 #Here we are declaring a variable to stroage the problems who can be solved.
for count in range(0, problems):
    answers = str(input())
    votes = 0
    for letter in answers:
        if letter == '1':
            votes += 1
    if votes >= 2:
        problemsfinished += 1
print(problemsfinished)