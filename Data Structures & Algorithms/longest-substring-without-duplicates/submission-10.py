class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = set()
        ptr1 = 0
        ptr2 = 0
        maxCount = 0
        while ptr2<len(s):
            if s[ptr2] not in hash:
                hash.add(s[ptr2])
                ptr2+=1
                maxCount = max(maxCount, ptr2-ptr1)
            else:
                hash.remove(s[ptr1])
                ptr1 += 1
                
        return maxCount

                