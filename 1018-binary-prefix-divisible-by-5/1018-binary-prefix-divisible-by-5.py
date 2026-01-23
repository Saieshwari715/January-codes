class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        arr=[]
        s=""
        for i in nums:
            s+=str(i)
            d=int(s,2)
            if(d%5==0):
                arr.append(True)
            else:
                arr.append(False)
        return arr




            
       
        