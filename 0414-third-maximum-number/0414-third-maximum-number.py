class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n=set(nums)
        c=sorted(n)
        l=len(c)
        if l==0:
            return Null
        elif l==2 or l==1:
            return c[-1]
        else:
            return c[-3]
        