import random
rolls = {}
for _ in range(10000):
    result = random.randint(1, 6)
    rolls[result] = rolls.get(result, 0) + 1
for face in sorted(rolls):
    count = rolls[face]
    bar = "█" * (count // 100)
    print(f"{face}: {bar} ({count})")