class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d = {}

        for i in nums:
            if i % 2 == 0:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1

        if not d:
            return -1

        maximum = max(d.values())
        ans = -1

        for keys, values in d.items():
            if values == maximum:
                if ans == -1 or keys < ans:
                    ans = keys

        return ans