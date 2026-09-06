class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash = set()
        maxCount = 0
        count = {}
        l = 0
        r = 0
        res = 0
        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            maxCount = max(maxCount, count[s[r]])
            if r-l - maxCount +1 > k:
                count[s[l]] -= 1
                l+=1
            res = max(res, r - l + 1)
            r+=1
        return res
            