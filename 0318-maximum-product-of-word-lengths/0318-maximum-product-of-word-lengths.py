class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maxi = 0

        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not set(words[i]) & set(words[j]):
                    maxi = max(maxi, len(words[i]) * len(words[j]))
        return maxi

        