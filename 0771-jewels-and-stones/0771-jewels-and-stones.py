class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        i = 0
        for stone in stones:
            if stone in jewels:
                i += 1
        return i