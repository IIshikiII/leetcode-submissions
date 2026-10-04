from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return[]
        
        window_size = len(p)
        p = Counter(p)
        start_counter = Counter(s[0:window_size])

        indices = []
        if p == start_counter:
            indices.append(0)
        # print(start_counter)
        for i in range(0, len(s) - window_size):
            start_counter[s[i]] -= 1
            start_counter[s[i+window_size]] = start_counter.get(s[i+window_size], 0) + 1
            if start_counter[s[i]] == 0:
                del start_counter[s[i]]
            # print(start_counter)
            
            if p == start_counter:
                indices.append(i+1)
        
        return indices

        