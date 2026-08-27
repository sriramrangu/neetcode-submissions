class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = dict()
        for num in nums:
            if num in hm:
                return True
            else:
                hm[num] = 1
        return False
        