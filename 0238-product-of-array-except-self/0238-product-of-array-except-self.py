class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        product = 1
        left = 0
        l = []
        while i < n:
            l.append(product)
            product = product*nums[i]
            i += 1
        right_product = 1
        i = n - 1

        while i >= 0:
            l[i] = l[i] * right_product
            right_product = right_product * nums[i]
            i -= 1
        return l
              