from collections import Counter, defaultdict

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        counter = Counter(list(moves))


        letters = defaultdict(lambda: 0)
        for direction, count in counter.most_common():
            letters[direction] = count

        if letters['L'] == letters['R'] and letters['U'] == letters['D']:
            return True
        else:
            return False