class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        positive_count = 0
        neg_count = 0
        for i in range(len(nums)):
            if nums[i] < 0 :
                neg_count += 1
            elif nums[i] > 0:
                positive_count += 1
        if neg_count >= positive_count:
            return neg_count
        else:
            return positive_count

        