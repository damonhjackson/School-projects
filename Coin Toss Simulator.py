import random

n = input("Enter number of experiments: ")
ctr_heads = 0
ctr_tails = 0

for i in range(0, int(n)):
    r = random.random()
    if r <= 0.5:
        print("Heads")
        ctr_heads = ctr_heads + 1
    else:
        print("Tails")
        ctr_tails = ctr_tails + 1
print("Number of Heads: " + str(ctr_heads))
print("Number of Tails: " + str(ctr_tails))

