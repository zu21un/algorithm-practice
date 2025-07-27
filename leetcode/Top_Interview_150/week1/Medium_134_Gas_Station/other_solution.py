class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        whole_length = len(gas)
        whole_sum = 0

        for i in range(whole_length):
            whole_sum += gas[i] - cost[i]
        
        if whole_sum < 0:
            return -1
        
        start = tank = 0
        for i in range(whole_length):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        
        return start
