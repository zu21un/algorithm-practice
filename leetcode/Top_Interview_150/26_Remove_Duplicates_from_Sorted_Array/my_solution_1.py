class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = sorted(list(set(nums)))

        for i, r in enumerate(result):
            nums[i] = r

        return len(result)

