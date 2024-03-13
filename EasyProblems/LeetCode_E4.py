#This Problem might be a bit tricky for new people
#First idea is to go through all of them but that's not efficient.
#Let's think of a smarter way.
#Sort list -> Most difference between first and last number
#Compare and then submit answer if there's a difference.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        strs = sorted(strs)
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] != strs[-1][i]:
                return ans
            ans += strs[0][i]
        return ans
