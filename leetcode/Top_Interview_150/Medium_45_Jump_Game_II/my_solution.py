class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums) - 1

        if goal == 0:
            return 0

        cnt_arr = [float('inf') for _ in range(len(nums))]

        current = 0
        cnt_arr[0] = 0

        while cnt_arr[-1] == float('inf'):
            jump = current + nums[current]
            jump_cnt = cnt_arr[current] + 1
            for j in range(current + 1, min(jump + 1, len(cnt_arr))):
                cnt_arr[j] = min(cnt_arr[j], jump_cnt)
            current += 1
            
        return cnt_arr[-1]
            
        