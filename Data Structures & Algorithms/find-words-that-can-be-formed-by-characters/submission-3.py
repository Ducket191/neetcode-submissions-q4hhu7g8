class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        for word in words:
            x = len(word)
            if all(word.count(c) <= chars.count(c) for c in set(word)):
                res += x
        return res