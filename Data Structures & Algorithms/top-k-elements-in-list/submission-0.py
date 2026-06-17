class Solution:
    def topKFrequent(self, nums, k):
        vals = set(nums)
        dic = {}
        for val in vals:
            dic[val] = 0
            for i in nums:
                if i == val:
                    dic[val] += 1
        items = []
        for key in dic:
            items.append((dic[key], key)) 
        items.sort(reverse=True)  
        toRet = []
        for i in range(k):
            toRet.append(items[i][1])  
        return toRet