class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        L , R = 0 , len(nums) - 1
        while L <= R :
            m = L + ((R-L) // 2)
            if nums[m] == target:
                return m 
            elif nums[m] > target:
                R = m - 1
            else : 
                L = m + 1
        return L