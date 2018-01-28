import time, random
difficulty = 2 + int(input("Choose the dificulty, 3 for easy, 2 for normal, 1 for HARD: "))
difficulty2 =difficulty
clues = list()
def generator():
    secret = str(random.randint(0, 999))
    if len(secret) == 3:
        pass
    else:
        for a in range(1, 4 - len(secret)):
            secret = "0" + secret
            # if the random number isn't 3 numbers large it fix them.
    return secret
# CLUES


while difficulty2 > 0:
    clues.append(generator())
    difficulty2 = difficulty2 -1

code = generator()

print(clues)
print(code + "code")
for a in range(0, difficulty):
    for b in list(clues[a]):
        for c in code:
            if b == c:
                print(a)
                print(b)

                print(str(c) + "==" + str(b))


