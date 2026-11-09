#Austin Hastings
#CMP 131 86520
#Week 8
#Lab 1
#29 OCT 2026
#Loop Patterns
print("------------")
print("Pattern A")

for i in range(1,11):
    for j in range(i):
        print("+", end="")
    print()


print("-------------")
print("Pattern B")

for i in range(10, 0, -1):
    for j in range(i):
        print("+", end="")
    print()