class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        toRet = []
        for i in range(len(nums)): 
            count = 1
            temp = nums
            num = temp.pop(i)
            for val in temp: 
                count *= val
            toRet.append(count) 
            temp.insert(i,num)
        return toRet
        

