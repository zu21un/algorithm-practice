class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        rotated = [0 for _ in range(nums_len)]
        
        step_remainer = k % nums_len
        
        for i in range(nums_len):
            rotated[(i + step_remainer) % nums_len] = nums[i]
        
        nums[:] = rotated[:]
        