from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        dic= Counter(nums)
        d=sorted(dic,key=dic.get,reverse=True)
        res=d[:k]
        
        return res

        '''
        res=[]
        dic= dict(Counter(nums))
        l=list(dic.values())
        sort_l=sorted(l,reverse=True)[:2]
        for i in sort_l:
            for key,val in dic.items():
                if i==val:
                    res.append(key)
        return res
        '''
        