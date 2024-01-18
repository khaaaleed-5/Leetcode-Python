from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        my_stack = deque()
        for i in s:
            if i == '(' or i == '[' or i == '{':
                my_stack.append(i)
            else:
                c = my_stack.pop()
                if i == ')' and c == '(':
                    continue
                elif i == ']' and c == '[':
                    continue
                elif i == '}' and c == '{':
                    continue
                else:
                    return False
        if len(my_stack):
            return False
        return True