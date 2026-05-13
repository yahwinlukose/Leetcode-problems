class Solution(object):
    def isPalindrome(self, x):
        
        rev = 0
        y = str(x)
        if y == y[::-1]:
            return True
        else:
            return False

        
        
