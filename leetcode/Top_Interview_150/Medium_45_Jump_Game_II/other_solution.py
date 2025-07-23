class Solution:
    def jump(self, nums: List[int]) -> int:
        near = far = jump_cnt = 0

        while far < len(nums) - 1:
            fartest = 0
            for i in range(near, far + 1):
                fartest = max(fartest, i + nums[i])
            
            near = far + 1
            far = fartest
            jump_cnt += 1
        
        return jump_cnt
            
        