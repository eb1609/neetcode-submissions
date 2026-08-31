class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x in "({[":
                stack.append(x)
            elif x in ")":
                if not stack or stack.pop()!="(":
                    return False
            elif x in "]":
                if not stack or stack.pop()!="[":
                    return False
            elif x in "}":
                if not stack or stack.pop()!="{":
                    return False
        return len(stack) == 0
        
