class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for ch in s:
            if ch == '[' or ch == '(' or ch == '{':
                st += [ch]
            else:
                if not st or (ch == ']' and st.pop() != '[') or (ch == ')' and st.pop() != '(') or (ch == '}' and st.pop() != '{'):
                    return False
                else:
                    continue
        return True if not st else False
