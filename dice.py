import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1, self.sides))


# 6-sided die
print("Rolling a 6-sided die:")
die1 = Die()

for _ in range(10):
    die1.roll_die()

# 10-sided die
print("=== 10-sided die rolls ===")
print("\n10-sided die rolls:")
die2 = Die(10)

for _ in range(10):
    die2.roll_die()

# 20-sided die
print("=== 20-sided die rolls ===")
print("\n20-sided die rolls:")
die3 = Die(20)

for _ in range(10):
    die3.roll_die()

