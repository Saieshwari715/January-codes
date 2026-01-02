class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic={}
        for i in words:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        sor = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
        r=[]
        for i in range(k):
            r.append(sor[i][0])
        return r

        