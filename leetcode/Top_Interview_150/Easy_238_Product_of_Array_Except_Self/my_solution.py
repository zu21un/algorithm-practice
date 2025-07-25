class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_all = 1
        zero_cnt = 0

        for num in nums:
            if num == 0:
                zero_cnt += 1
                continue

            product_all *= num
        
        if zero_cnt > 1:
            return [0 for _ in range(len(nums))]
        
        if zero_cnt == 1:
            answer = [0 for _ in range(len(nums))]
            zero_idx = nums.index(0)
            answer[zero_idx] = product_all

            return answer

        answer = []
        for num in nums:
            answer.append(int(product_all/num))
        
        return answer