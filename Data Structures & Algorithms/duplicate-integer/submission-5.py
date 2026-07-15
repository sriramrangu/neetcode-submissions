class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        # flag = False
        hm = set()
        for i in range(n):
            if nums[i] in hm:
                return True
            hm.add(nums[i])
        return False
        