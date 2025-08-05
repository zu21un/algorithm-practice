class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1

        dic = {}

        for idx, rating in enumerate(ratings):
            if rating not in dic:
                dic[rating] = []
            dic[rating].append(idx)
        
        candies = [1 for _ in range(len(ratings))]
        for key in sorted(dic.keys()):
            for idx in dic[key]:
                # first index
                if idx == 0:
                    if ratings[idx] <= ratings[idx+1]:
                        continue
                    candies[idx] = candies[idx+1] + 1
                
                # last index
                elif idx == len(ratings) - 1:
                    if ratings[idx] <= ratings[idx-1]:
                        continue
                    candies[idx] = candies[idx-1] + 1
                else:
                    if ratings[idx] <= ratings[idx-1] and ratings[idx] <= ratings[idx+1]:
                        continue
                    if ratings[idx] > ratings[idx-1] and ratings[idx] > ratings[idx+1]:
                        candies[idx] = max(candies[idx-1], candies[idx+1]) + 1
                        continue
                    if ratings[idx] > ratings[idx-1]:
                        candies[idx] = candies[idx-1] + 1
                        continue
                    if ratings[idx] > ratings[idx+1]:
                        candies[idx] = candies[idx+1] + 1 

        return sum(candies)
        
        
        