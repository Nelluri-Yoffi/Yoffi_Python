class deckOfCards:
    def hasGroupsSizeX(self, deck):
        count = {}
        for card in deck:
            if card in count:
                count[card] = count[card] + 1
            else:
                count[card] = 1

        counts_list = list(count.values())
        smallest = min(counts_list)

        for x in range(2, smallest + 1):
            works = True
            for c in counts_list:
                if c % x != 0:
                    works = False
            if works:
                return True

        return False
sol = deckOfCards()
deck1 = [1, 2, 3, 4, 4, 3, 2, 1]
print(sol.hasGroupsSizeX(deck1))
deck2 = [1, 1, 1, 2, 2, 2, 3, 3]
print(sol.hasGroupsSizeX(deck2))