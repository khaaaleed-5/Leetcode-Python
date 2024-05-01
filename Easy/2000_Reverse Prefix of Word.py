class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        s = set(word)
        if ch not in s:
            return word
        word_idx = word.index(ch) + 1
        new_word = word[:word_idx][::-1] + word[word_idx:]

        return new_word
