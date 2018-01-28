import time, random
difficulty = 2 + int(input("Choose the dificulty, 3 for easy, 2 for normal, 1 for HARD: "))
clues = list()
def generator():
    secret = str(random.randint(0, 999))
    if len(secret) == 3:
        pass
    else:
        for a in range(1, 4 - len(secret)):
            secret = "0" + secret
            # if the random number isn't 3 numbers large it fix them
    print("DONE")
    return secret
# CLUES


while difficulty > 0:
    clues.append(generator())
    difficulty = difficulty -1

code = generator()

print(clues)
print(code + "code")
for a in range(0, 5):
    print(a)
    for b in clues[a]:
        print(b +"hola")
        for c in code:
            if b == c:
                print(str(c) +"==" +str(b))


