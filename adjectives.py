import random
adjectives = ["magnificent", "chaotic", "questionable", "legendary", "suspicious"]
nouns = ["potato", "wizard", "raccoon", "genius", "goblin"]
def generate_title():
    return f"You are a {random.choice(adjectives)} {random.choice(nouns)}."
for _ in range(5):
    print(generate_title())