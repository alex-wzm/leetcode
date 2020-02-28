from typing import List
import time
import pandas as pd
import numpy as np

class Solution: # ACCEPTED
    def maxSubArray(self, nums: List[int]) -> int:

        # init output to min_value and
        # init accumulator "current_max"
        max_so_far = float('-inf')
        current_max = 0
        
        for i in range(0, len(nums)):
            # accumulate current_max
            current_max = current_max + nums[i]

            # store if max sum so far
            if max_so_far < current_max:
                max_so_far = current_max
            
            # reset accumulator if value < 0
            # i.e. restart counting with next sub-array
            if current_max < 0:
                current_max = 0
                
        return max_so_far
        """
        Analysis:
            - O(n) time
            - O(n) space
        """
        

# class Solution: # OUTPUT LIMIT EXCEEDED
#     def maxSubArray(self, nums: List[int]) -> int:

#         # base case
#         if len(nums) == 1:
#             # NOTE: is this a significant improvement?
#             return nums[0]
        
#         # init output to min_value
#         max_so_far = float('-inf')
        
#         # compare all sub arrays by recursively by storing max of
#         # - max_so_far
#         # - sum of nums (current sub array)
#         # - and sum of nums[i:-1] (pop current sub array)
#         for i in range(0, len(nums)):
#             max_so_far = max(
#                 max_so_far,
#                 sum(nums[i:]),
#                 self.maxSubArray(nums[i:-1])
#             )
            
#         return max_so_far

### TEST CODE ###

s = Solution()

test_cases = {
    # expected_output: case
    6: [-2,1,-3,4,-1,2,1,-5,4],
    1: [-2, 1],
    3: [-2, 1, 2],
    -3: [-84,-87,-78,-16,-94,-36,-87,-93,-50,-22,-63,-28,-91,-60,-64,-27,-41,-27,-73,-37,-12,-69,-68,-30,-83,-31,-63,-24,-68,-36,-30,-3,-23,-59,-70,-68,-94,-57,-12,-43,-30,-74,-22,-20,-85,-38,-99,-25,-16,-71,-14,-27,-92,-81,-57,-74,-63,-71,-97,-82,-6,-26,-85,-28,-37,-6,-47,-30,-14,-58,-25,-96,-83,-46,-15,-68,-35,-65,-44,-51,-88,-9,-77,-79,-89,-85,-4,-52,-55,-100,-33,-61,-77,-69,-40,-13,-27,-87,-95,-40]
}

# test_cases = {
#     -14: [-14,-84,-87,-78,-45,-94,-36,-87,-93,-50,-22,-63,-28,-91,-60],
#     -15: [-15,-84,-87,-78,-45,-94,-36,-87,-93,-50,-22,-63,-28,-91,-60,-64],
#     -16: [-16,-84,-87,-78,-45,-94,-36,-87,-93,-50,-22,-63,-28,-91,-60,-64,-27],
#     -17: [-17,-84,-87,-78,-45,-94,-36,-87,-93,-50,-22,-63,-28,-91,-60,-64,-27,-41],
#     -18: [-18,-84,-87,-78,-45,-94,-36,-87,-93,-50,-22,-63,-28,-91,-60,-64,-27,-41,-27],
#     -19: [-19,-84,-87,-78,-45,-94,-36,-87,-93,-50,-22,-63,-28,-91,-60,-64,-27,-41,-27,-73],
#     -20: [-20,-84,-87,-78,-45,-94,-36,-87,-93,-50,-22,-63,-28,-91,-60,-64,-27,-41,-27,-73,-37],
#     -21: [-21,-84,-87,-78,-45,-94,-36,-87,-93,-50,-22,-63,-28,-91,-60,-64,-27,-41,-27,-73,-37,-69],
#     -22: [-22,-84,-87,-78,-45,-94,-36,-87,-93,-50,-22,-63,-28,-91,-60,-64,-27,-41,-27,-73,-37,-69,-99],
#     -23: [-23,-84,-87,-78,-45,-94,-36,-87,-93,-50,-22,-63,-28,-91,-60,-64,-27,-41,-27,-73,-37,-69,-99,-54],
#     -24: [-24,-84,-87,-78,-45,-94,-36,-87,-93,-50,-22,-63,-28,-91,-60,-64,-27,-41,-27,-73,-37,-69,-99,-54,-51]
# }

completion_times = []

count_passes = 0

for expected_output, test in test_cases.items():
    print("="*50)
    print(f"INPUT: {test}")

    start = time.time()
    output = s.maxSubArray(test)
    completion_times.append([len(test),(time.time() - start)])

    print(f"OUTPUT: {output}")
    print(f"EXPECTED: {expected_output}\n")
    
    if output == expected_output:
        print("PASS")
        count_passes += 1
    else:
        print("FAIL")



print("="*50)
print(f"Passed {count_passes}/{len(test_cases)} test cases.")
print()

print(f"Performance:")
df = pd.DataFrame(np.array(completion_times), columns=['n', 'time'])
# df.to_pickle("../../../Code/Tools/plot/data/53_max_subarray.pkl") # uncomment to log performance
print(df)