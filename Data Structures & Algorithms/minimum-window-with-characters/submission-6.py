class Solution:

    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""

        count1 = {}
        count2 = {}

        for char in t:
            count1[char] = count1.get(char, 0) + 1

        need = len(count1)
        have = 0

        l = 0
        r = 0

        window = len(s) + 1
        bestL = 0
        bestR = 0

        while r < len(s):

            count2[s[r]] = count2.get(s[r], 0) + 1

            if s[r] in count1 and count2[s[r]] == count1[s[r]]:
                have += 1

            while have == need:

                if r - l + 1 < window:
                    window = r - l + 1
                    bestL = l
                    bestR = r

                count2[s[l]] -= 1

                if s[l] in count1 and count2[s[l]] < count1[s[l]]:
                    have -= 1

                l += 1

            r += 1

        if window == len(s) + 1:
            return ""

        return s[bestL:bestR + 1]