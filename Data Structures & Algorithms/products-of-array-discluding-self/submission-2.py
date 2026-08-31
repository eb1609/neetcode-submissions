class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        pre.append(nums[0])
        for n in range(1, len(nums)):
            pre.append(nums[n]*pre[n-1])
        suf = []
        suf.append(nums[len(nums)-1])
        for i in range(len(nums)-2,-1,-1):
            suf.append(nums[i]*suf[-1])
        suf.reverse()
        result = []
        for x in range(len(nums)):
            if x == 0:
                result.append(suf[1])
            elif x == len(nums) - 1:
                result.append(pre[x-1])
            else:
                result.append(pre[x-1]*suf[x+1])
        return result
            

