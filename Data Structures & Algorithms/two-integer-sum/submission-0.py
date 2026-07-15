class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_m = dict()
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in h_m:
                return [h_m[rem], i]
            else:
                h_m[nums[i]] = i
        