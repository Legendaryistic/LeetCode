#For starters, this question is asking for the indices.
#Remember list indices go from 0 to n
#You cannot choose the same index twice.
#You can brute force this problem!
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
