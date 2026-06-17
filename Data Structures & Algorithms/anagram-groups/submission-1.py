class Solution:
    def groupAnagrams(self, strs):
        toRet = []
        seen = set()
        
        for i in range(len(strs)):
            if i in seen:
                continue
            
            group = [strs[i]]
            seen.add(i)
            
            for j in range(i + 1, len(strs)):
                if j not in seen and sorted(strs[i]) == sorted(strs[j]):
                    group.append(strs[j])
                    seen.add(j)
            
            toRet.append(group)
        
        return toRet