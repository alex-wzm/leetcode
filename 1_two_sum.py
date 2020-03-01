from typing import List
from collections import defaultdict

class Solution2: # Accepted
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # init hash table to store indices of elements by value
        # using defaultdict to init values as list types
        # so appending indices of duplicates is easier
        hash_table = defaultdict(list)

        # populate hash table
        for i, n in enumerate(nums):
            hash_table[n].append(i)

        # iterate through list searching hash table for compliment
        # this is safe because a target pair is guaranteed
        for i, n in enumerate(nums):
            if target - n in hash_table:
                # when compliment is found, search for non-duplicate element
                # by ensuring indices are different
                for j in hash_table[target - n]:
                    if i != j:
                        return [i, j]
                        """
                        Analysis:
                        - Time: O(n)
                        - Space: O(n)
                        """


        
class Solution1: # Time Limit Exceeded
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # brute force
        for i, n1 in enumerate(nums):
            for j, n2 in enumerate(nums):
                if i != j:
                    if n1 + n2 == target:
                        return [i, j]
                        """
                        Analysis:
                        - Time: O(n^2)
                        - Space: O(1)
                        """
 


### TEST CODE ###

s = Solution2()

test_cases = [
    ([0,1], ([1,1,2], 2)),
    ([0,1], ([2,7,11,15], 9)),
    ([1,2], ([3,2,4], 6)),
    ([2,4], ([3,1,4,2,7,5], 11)),
]

count_passes = 0

for expected_output, test in test_cases:
    print("="*50)
    print(f"INPUT: {test}")

    output = s.twoSum(test[0], test[1])

    print(f"OUTPUT: {output}")
    print(f"EXPECTED: {expected_output}\n")
    
    if output == expected_output:
        print("PASS")
        count_passes += 1
    else:
        print("FAIL")

print("="*50)
print(f"Passed {count_passes}/{len(test_cases)} test cases.\n")
