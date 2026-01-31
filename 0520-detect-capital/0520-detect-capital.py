class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        u=word.upper()
        l=word.lower()
        i=0
        if word==u or word==l or word[0]==u[0] and word[i+1:]==l[i+1:]:
            return True
        return False