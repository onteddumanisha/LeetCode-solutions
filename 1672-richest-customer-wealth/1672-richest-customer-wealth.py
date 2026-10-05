class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        greatest = 0
        for i in accounts:
            wealth = sum(i)
            if wealth > greatest:
                greatest = wealth
        return greatest


        