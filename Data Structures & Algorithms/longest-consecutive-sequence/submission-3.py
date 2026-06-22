class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:        
        uniqueNums = set(nums) 
        count = 0
        
        for n in uniqueNums:
            if n - 1 not in uniqueNums:
                temp = 1
                current = n
                while current + 1 in uniqueNums:
                    current += 1
                    temp += 1
                count = max(count, temp)
        
        return count
