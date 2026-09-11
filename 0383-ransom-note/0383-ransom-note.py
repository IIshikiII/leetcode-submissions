class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = dict()
        for char in magazine:
            magazine_dict[char] = magazine_dict.get(char, 0) + 1
        
        for char in ransomNote:
            magazine_dict[char] = magazine_dict.get(char, 0) - 1
            if magazine_dict[char] < 0:
                return False
        
        return True