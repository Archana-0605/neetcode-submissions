class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lp = [1] * n
        rp = [1] * n
        for i in range(1,n):
            lp[i] = lp[i-1]*nums[i-1]

        for j in range(n-2,-1,-1):
            rp[j] = rp[j+1]*nums[j+1]
        result = [lp[k]*rp[k] for k in range(n)]
        return result