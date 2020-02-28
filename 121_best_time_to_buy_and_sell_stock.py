from typing import List

class Solution2: # Accepted
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) < 1:
            return 0

        max_profit_so_far = 0
        min_buy_so_far = max(prices)

        for i, price in enumerate(prices):
            # if price < min_buy_so_far then update min_buy_so_far
            # this is not an opportunity to calculate max_profit
            if price < min_buy_so_far:
                min_buy_so_far = price
            # if not updating min_buy_so_far then calculate potential max_profit
            else:
                max_profit_so_far = max(max_profit_so_far, price - min_buy_so_far)

        return max_profit_so_far
        """
        Analysis:
        - Time: O(n)
        - Space: O(1)
        """

class Solution1: # Time Limit Exceeded
    def maxProfit(self, prices: List[int]) -> int:

        max_profit_so_far = 0

        for i, price1 in enumerate(prices):
            for j, price2 in enumerate(prices[i:]):
                if price2 > price1:
                    max_profit_so_far = max(max_profit_so_far, price2-price1)

        return max_profit_so_far
        """
        Analysis:
        - Time: O(n^2)
        - Space: O(1)
        """


        
### TEST CODE ###

s = Solution1()

test_cases = [
    (0, []),
    (0, [0]),
    (0, [1]),
    (0, [1,1,1]),
    (0, [-1,-1,-1]),
    (2, [1,2,3]),
    (0, [3,2,1]),
    (5, [7,1,5,3,6,4]),
    (0, [7,6,4,3,1]),
    (6, [7,6,4,3,1,7]),
    (2, [2,3,4,1]),
]

count_passes = 0

for expected_output, test in test_cases:
    print("="*50)
    print(f"INPUT: {test}")

    output = s.maxProfit(test)

    print(f"OUTPUT: {output}")
    print(f"EXPECTED: {expected_output}\n")
    
    if output == expected_output:
        print("PASS")
        count_passes += 1
    else:
        print("FAIL")

print("="*50)
print(f"Passed {count_passes}/{len(test_cases)} test cases.\n")
