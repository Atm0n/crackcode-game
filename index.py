import time, random
difficulty = 2 + int(input("Choose the dificulty, 3 for easy, 2 for normal, 1 for HARD: "))
difficulty2 = difficulty
attempts = 0
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
print(range(0, len(clues)-1))
print("CLUES")
for a in clues:
    for d in range(0, len(a)):
        for c in range(0, len(code)):
            if a[d] == code[c]:
                if d == c:
                    print(str(a) + " There's a number well placed")
                else:
                    print(str(a) + " There's a number wrong placed")
            else:
                pass


while code != str(int(input("Enter a 3 number lenght code: "))):
    pass
print("Ho has aconseguit!")
