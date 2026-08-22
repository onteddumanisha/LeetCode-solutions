class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        for keys,value in freq.items():
            if value > 1:
                return keys


        