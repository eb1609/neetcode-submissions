class Solution:

    def encode(self, strs: List[str]) -> str:
        str1 = ""
        for s in strs:
            str1 += str(len(s)) + "#" + s
        return str1
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            word = s[j + 1 : j + 1 + length]
            result.append(word)

            i = j + 1 + length

        return result
            
