class Solution:
    def numberOfSteps(self, nums: int) -> int:
        count = 0
        while nums >0:
            if nums % 2 == 0:
                nums = nums// 2
            elif nums % 2!= 0:
                nums = nums -1
            count += 1
        return count
        