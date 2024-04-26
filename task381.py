import random
class RandomizedCollection:

    def __init__(self):
        self.vals = [] # record current values
        self.index = {} # record index for same value

    def insert(self, val: int) -> bool:
        self.vals.append(val)
        if val in self.index: self.index[val].append(len(self.vals)-1)
        else: self.index[val] = [len(self.vals)-1]
        return len(self.index[val]) == 1

    def remove(self, val: int) -> bool:
        if val not in self.vals: return False
        current_index = self.index[val].pop()
        last_element = self.vals[-1]
        # remove the last one in self.vals and place it in the place of the element which is supposed to be removed
        self.vals[current_index] = last_element
        # have to append then remove -- in case self.index[last_element] is empty
        self.index[last_element].append(current_index)
        self.index[last_element].remove(len(self.vals)-1)
        self.vals.pop()
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.vals)
    


obj = RandomizedCollection()
param_1 = obj.insert(1)
print(obj.vals)
param_2 = obj.remove(1)
print(obj.vals)
param_1 = obj.insert(1)
print(obj.vals)

# param_3 = obj.getRandom()
# print(obj.vals)