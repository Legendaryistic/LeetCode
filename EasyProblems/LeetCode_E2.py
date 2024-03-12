#Welcome back to another poorly made solution.
#This time, we can be lazy ;>
#This problem is easy. Check if it's a palindrome, if it isn't return false!
#Check the negative numbers though.
#As you can see, -121 is not a palindrome because it becomes 121- litteraly.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False
