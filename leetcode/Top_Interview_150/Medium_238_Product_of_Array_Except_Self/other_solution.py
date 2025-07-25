class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_cnt = len(nums)
        answer = [1 for _ in range(num_cnt)]

        left = 1
        for i, num in enumerate(nums):
            answer[i] *= left
            left *= num
        
        right = 1

        for j, num in enumerate(nums[::-1]):
            answer[num_cnt - j - 1] *= right
            right *= num
        
        return answer