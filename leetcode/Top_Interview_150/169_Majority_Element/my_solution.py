class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = {}
        
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 0
            nums_dict[num] += 1

        for k in nums_dict.keys():
            if nums_dict[k] <= (len(nums) / 2):
                continue

            return k
            