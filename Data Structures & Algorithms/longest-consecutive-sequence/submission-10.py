class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        maxCount = 0
        count = 0
        for n in nums:
            seen.add(n)
        for n in nums:
            if n-1 not in seen:
                x = 1
                count = 1
                while n+x in seen:
                    count+=1
                    x+=1
                if count > maxCount:
                    maxCount = count
        return maxCount