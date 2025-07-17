class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0

        for num in nums[1:]:
            if num == nums[index]:
                continue
            nums[index + 1] = num
            index += 1
        
        return index + 1
