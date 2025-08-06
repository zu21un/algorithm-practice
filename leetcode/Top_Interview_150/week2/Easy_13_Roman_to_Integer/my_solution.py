class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        nums = []
        for symbol in s:
            nums.append(roman_dict[symbol])

        i = 0
        answer = 0
        while i < len(nums):
            if i < len(nums) - 1 and nums[i] < nums[i+1]:
                answer += nums[i+1] - nums[i]
                i += 2
                continue
            
            answer += nums[i]
            i += 1
            

        return answer
        