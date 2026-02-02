class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cset=set()
        ml=0
        l=0
        n=len(s)
        for r in range(n):
            if s[r] not in cset:
                cset.add(s[r])
                ml=max(ml,r-l+1)
            else:
                while(s[r] in cset):
                    cset.remove(s[l])
                    l+=1
                cset.add(s[r])
        return ml
        
        