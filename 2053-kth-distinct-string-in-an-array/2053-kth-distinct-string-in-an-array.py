class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dict={}
        u=[]
        for i in arr:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        for i in arr:
            if(dict[i]==1):
                u.append(i)
        for i in range(len(u)):
            if(i==k-1):
                return u[i]
        return ""
        

        