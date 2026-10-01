class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_table = dict()
        used = set()
        for idx, char in enumerate(s):
            if char not in hash_table and t[idx] not in used:
                hash_table[char] = t[idx]
                used.add(t[idx])
            elif char not in hash_table and t[idx] in used:
                return False
            elif hash_table[char] == t[idx]:
                continue
            else:
                return False
        
        return True


        