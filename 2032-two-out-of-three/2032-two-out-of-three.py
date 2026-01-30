class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        
        s1,s2,s3=set(nums1),set(nums2),set(nums3)
        a=[]
        
        for i in s1|s2|s3:
            c=0
            if i in s1:c+=1
            if i in s2:c+=1
            if i in s3:c+=1

            if c>=2:
                a.append(i)
        return a
        



        