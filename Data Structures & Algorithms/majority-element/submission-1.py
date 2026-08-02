class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Booyer moore algo 
        ele = count = 0
        for i in nums:
            if count == 0:
                count += 1
                ele = i
            else:
                if i == ele:
                    count += 1
                else:
                    count -= 1
        return ele