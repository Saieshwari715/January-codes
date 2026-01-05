class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        dic={}
        paragraph = paragraph.lower()

        for ch in ".,!?;'":  
            paragraph = paragraph.replace(ch, " ")
        for i in paragraph.split():
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        sor = dict(sorted(dic.items(), key=lambda x: (x[1], x[0]), reverse=True))
        for i in sor:
            if i not in banned:
                return i
                break
        
        