class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = dict()
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in hm:
                return [hm[rem] , i]
            else:
                hm[nums[i]] = i