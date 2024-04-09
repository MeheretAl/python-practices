class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        total = 0
        #needs you know what
        for i, x in enumerate(tickets):
            if i <= k:
                total += min(tickets[i], tickets[k])
            else:
                total += min(tickets[i], tickets[k] - 1)

        return total