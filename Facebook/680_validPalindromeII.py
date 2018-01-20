class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # O(n), O(1)         
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return self.isPalindrome(s, l+1, r) or self.isPalindrome(s, l, r-1)
            l += 1; r -= 1
        return True
    
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]: return False
            l += 1; r -= 1
        return True