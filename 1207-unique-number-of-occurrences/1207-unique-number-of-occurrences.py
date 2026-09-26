class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        ans = {}
        for i in range(len(arr)):
            if arr[i] in freq:
                freq[arr[i]] += 1
            else:
                freq[arr[i]] = 1
        for value in freq.values():
            if value in ans:
                return False
            else:
                ans[value] = 1
        return True
                


        