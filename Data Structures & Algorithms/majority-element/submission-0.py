class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele , count = 0,0
        for i in nums:
            if count == 0:
                ele = i
                count += 1
            else :
                if ele == i:
                    count += 1
                else :
                    count -= 1
        return ele
        