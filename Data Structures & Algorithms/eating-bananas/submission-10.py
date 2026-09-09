class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper = 0
        for p in piles:
            upper = max(upper,p)
        lower = 1
        while lower <= upper:
            med = (upper+lower)//2
            time = 0
            for p in piles:
                time += (p + med - 1) // med
            if time<=h:
                upper = med-1
            else:
                lower = med+1
        return lower

            