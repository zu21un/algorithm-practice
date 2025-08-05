class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        
        # find max index
        idx, max_height = 0, 0
        
        for i, h in enumerate(height):
            if h <= max_height:
                continue
            idx = i
            max_height = h

        water = 0
        
        i = idx
        while i > 1:
            # find next max
            left_idx, left_max = 0, 0
            for j in range(i-1, -1, -1):
                if height[j] < left_max:
                    continue
                left_idx = j
                left_max = height[j]
            if left_max == 0:
                break
            # compute water
            for k in range(i-1, left_idx, -1):
                water += left_max - height[k]
            i = left_idx

        # go right from max index
        i = idx
        while i < len(height) - 2:
            # find next max
            right_idx, right_max = 0, 0
            for j in range(i+1, len(height)):
                if height[j] < right_max:
                    continue
                right_idx = j
                right_max = height[j]
            if right_max == 0:
                break
            # compute water
            for k in range(i+1, right_idx):
                water += right_max - height[k]
            
            i = right_idx
                

        return water
            

        