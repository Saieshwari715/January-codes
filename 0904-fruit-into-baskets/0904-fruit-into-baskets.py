class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dict={}
        l=0
        ml=0
        n=len(fruits)
        for r in range(n):
            if fruits[r] in dict:
                dict[fruits[r]]+=1
            else:
                dict[fruits[r]]=1
            while len(dict)>2:
                dict[fruits[l]]-=1
                if dict[fruits[l]]==0:
                    del dict[fruits[l]]
                l+=1
            ml=max(ml,r-l+1)
        return ml
                    

        