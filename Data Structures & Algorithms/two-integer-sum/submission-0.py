class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in vals:
                return [vals[diff], i]
            vals[num] = i
        return []