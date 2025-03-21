class Solution:
    def reverseWords(self, s: str) -> str:

        words = s.split()
        print(words)
        rev = words[::-1]

        return " ".join(rev)

        