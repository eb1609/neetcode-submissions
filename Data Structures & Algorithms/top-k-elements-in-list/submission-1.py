class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = {}
        for n in nums:
            if n in groups:
                groups[n] +=1
            else:
                groups[n] = 1
        result = []
        sorted_groups = sorted(groups.items(), key=lambda x: x[1], reverse=True)

        for num, freq in list(sorted_groups):
            if k == 0:
                break
            result.append(num)
            k-=1
        return result