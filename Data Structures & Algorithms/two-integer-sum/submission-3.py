class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[]
        for i in range(len(nums)):
            a= nums[i]
            b= target-a
            if b in nums[i+1:] :
                idx=nums.index(b,i+1)
                res.extend([i,idx])
                break
        return res


        