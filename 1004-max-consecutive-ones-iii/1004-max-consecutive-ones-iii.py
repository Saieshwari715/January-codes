class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        ml=0
        n=len(nums)
        z=0
        for r in range(n):
            if nums[r]==0:
                z+=1
            
            while(z>k):
                if(nums[l]==0):
                    z-=1
                l+=1
            ml=max(ml,r-l+1)
        return ml
        