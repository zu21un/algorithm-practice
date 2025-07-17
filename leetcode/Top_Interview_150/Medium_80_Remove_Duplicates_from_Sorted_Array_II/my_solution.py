class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = j = 0

        removed = 0

        # cnt = 0 # for debug

        while i < len(nums) - removed:
            # print(f'loop #{cnt}:')
            current_num = nums[i]
            # print(f'    current_num, i: {current_num}, {i}')

            j = i
            next_num = nums[j]

            while j < len(nums) - removed:
                if nums[j] != current_num:
                    next_num = nums[j]
                    break
                else:
                    j += 1
                    continue
            # print(f'    next_num, j: {next_num}, {j}')
            
            
            diff = j - i

            if diff <= 2:
                # print(f'    difference is smaller than 2')
                i = j
                continue
            
            over = diff - 2

            # print(f'    difference is over {over}')

            # print(f'    len(nums) - over: {len(nums) - over}')
            for k in range(i + 2, len(nums) - over - removed):
                nums[k] = nums[k + over]
            
            # print(f'    after removed: {nums}')

            removed += over
            i += 2

            # cnt += 1

        return len(nums) - removed
                
        
        