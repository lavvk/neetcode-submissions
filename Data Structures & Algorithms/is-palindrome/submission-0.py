class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
        words = ""
        for ch in s.lower():
            if ch in alpha:
                words += ch
        check = ""
        for char in words:
            check = char + check
        return words == check

