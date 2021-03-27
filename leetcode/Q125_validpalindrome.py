class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # need s to delete characters which are not alphabets
        for i in range(32,127):
            if not ((i>=65 and i<=90) or (i>=97 and i<=122) or (i>=48 and i<=57)):
                s = s.replace(chr(i),"")
        
        front_idx = 0
        rear_idx = len(s)-1
        while front_idx < rear_idx:
            if s[front_idx].upper() != s[rear_idx].upper():
                return False
            front_idx+=1
            rear_idx-=1
            
        return True
