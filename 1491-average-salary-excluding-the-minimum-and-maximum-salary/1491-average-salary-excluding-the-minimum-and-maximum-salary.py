class Solution:
    def average(self, salary: List[int]) -> float:
        maxi=max(salary)
        mini=min(salary)
        a=[]
        for i in salary:
            if(i!=maxi and i!=mini):
                a.append(i)
        avg=sum(a)/len(a)
        return avg
        