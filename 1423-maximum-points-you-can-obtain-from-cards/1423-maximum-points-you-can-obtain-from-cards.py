class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        
        if(k==n):
            return sum(cardPoints)
        ts=sum(cardPoints)
        wsize=n-k
        wsum=sum(cardPoints[:wsize])
        minwsum=wsum
        for i in range(wsize,n):
            wsum+=cardPoints[i]-cardPoints[i-wsize]
            minwsum=min(minwsum,wsum)
        return ts-minwsum




        