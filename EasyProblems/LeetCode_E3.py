#Terrible Coding time!
class Solution:
    def romanToInt(self, s: str) -> int:
        s += 'O'
        ans = 0
        numerals = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1,'O':0}
        for i in range(len(s)-1):
            if numerals[s[i]] < numerals[s[i+1]]:
                ans -= numerals[s[i]]
            else:
                ans += numerals[s[i]]
        return ans
