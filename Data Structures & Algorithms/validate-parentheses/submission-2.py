class Solution:
    def isValid(self, s: str) -> bool:
        m = {
            ")": "(", 
            "}": "{", 
            "]": "[",
        }
        stack = []
        for b in s:
            start = m.get(b)
            is_closing_bracket = start is not None
            if is_closing_bracket:
                if not stack or stack[-1] != start:
                    return False
                stack.pop()
            else:
                stack.append(b)
        if stack:
            return False
        return True
