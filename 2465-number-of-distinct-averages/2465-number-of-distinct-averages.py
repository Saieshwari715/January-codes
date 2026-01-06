class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        c=0
        seen=[]
        while len(nums)>1:
            mini=min(nums)
            maxi=max(nums)
            avg=(mini+maxi)/2
                
                
            if avg not in seen:
                seen.append(avg)
               
            nums.remove(mini)
            nums.remove(maxi)
        return len(seen)


        