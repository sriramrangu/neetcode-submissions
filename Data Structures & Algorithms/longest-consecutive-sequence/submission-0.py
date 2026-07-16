class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hm = set()
        for num in nums:
            hm.add(num)

        res = 0
        for i in hm:
            x = i
            count = 1
            while x + 1 in hm:
                count += 1
                x += 1
            res = max(count, res)
        return res