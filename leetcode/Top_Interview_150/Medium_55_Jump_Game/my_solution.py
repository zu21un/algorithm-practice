class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        max_idx = 0
        current_idx = 0

        while current_idx <= max_idx and current_idx < len(nums) - 1:
            max_idx = max(max_idx, current_idx + nums[current_idx])
            
            if max_idx >= len(nums) - 1:
                return True
            current_idx += 1
        
        return False
        
        
        