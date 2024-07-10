from typing import List
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        if not customers: return 0
        current_time = customers[0][0] + customers[0][1]
        waiting_time = customers[0][1]
        for i in range(1, len(customers)):
            if current_time > customers[i][0]:
                current_time += customers[i][1]
                waiting_time += current_time - customers[i][0]
            else:
                current_time = customers[i][0] + customers[i][1]
                waiting_time += customers[i][1]
        return waiting_time / len(customers)
