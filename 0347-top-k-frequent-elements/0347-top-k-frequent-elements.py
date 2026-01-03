class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        sorted_dict = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
        a=[]
        for i in sorted_dict:
            a.append(i)
            if(len(a)==k):
                break
        return a
        


        