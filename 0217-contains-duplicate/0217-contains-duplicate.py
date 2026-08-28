class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for i in nums:
            if i  in freq:
                freq[i] += 1
                if freq[i] >1:
                    return True
            else:
                freq[i] = 1

        else:
            return False
        