class Solution:

    def makeGood(self, s: str) -> str:
        stack = []
        ptr = 0
        while ptr < len(s):
            if stack and stack[-1] != s[ptr] and stack[-1].lower() == s[ptr].lower():
                stack.pop()
            else:
                stack.append(s[ptr])

            ptr += 1

        return "".join(stack)
