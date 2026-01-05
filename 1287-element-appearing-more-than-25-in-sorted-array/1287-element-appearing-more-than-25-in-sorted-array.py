class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dic={}
        t=len(arr)
        for i in arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for key,value in dic.items():
            per=(value/t)*100
            if(per>25):
                return key

        