class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_cnt = {}
        for i in range(len(s)):
            char_cnt[s[i]] = char_cnt.get(s[i], 0) + 1
            char_cnt[t[i]] = char_cnt.get(t[i], 0) - 1
        return all(count == 0 for count in char_cnt.values())
        