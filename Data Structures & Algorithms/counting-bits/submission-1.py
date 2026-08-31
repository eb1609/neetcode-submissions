class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for i in range(n+1):
            count = 0
            for c in range(i+1):
                if i & (1<<c):
                    count+=1
            arr.append(count)
        return arr