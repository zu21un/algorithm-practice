class RandomizedSet:

    def __init__(self):
        self.values = []
        self.values_dict = {}

    def insert(self, val: int) -> bool:
        if val in self.values_dict:
            return False
        idx = len(self.values)
        self.values_dict[val] = idx
        self.values.append(val)

        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.values_dict:
            return False
        idx = self.values_dict[val]

        last_val = self.values[-1]

        self.values[idx] = last_val
        self.values.pop()

        del self.values_dict[val]

        if last_val in self.values_dict:
            self.values_dict[last_val] = idx

        return True
        

    def getRandom(self) -> int:
        return random.sample(self.values, 1)[0]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()