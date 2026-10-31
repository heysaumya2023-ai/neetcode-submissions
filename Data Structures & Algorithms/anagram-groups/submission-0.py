class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l={}
        for i in strs:
            j="".join(sorted(i))
            if j in l:
                l[j].append(i)
            else:
                l[j]=[i]
        return list(l.values())
    

            