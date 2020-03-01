from typing import List
from collections import defaultdict

class Solution: # Accepted
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Analysis:
        - Time: O(n)
        - Space: O(n)
        """

        # init hash table to store indices of elements by value
        # using defaultdict to init values as list types
        # so appending indices of duplicates is easier
        hash_table = defaultdict(list)

        for i, n in enumerate(numbers):
            # find compliment in hash table
            if target - n in hash_table:
                # when compliment is found, search for non-duplicate element
                # by ensuring indices are different
                for j in hash_table[target - n]:
                    # return such that i < j
                    if i != j:
                        return sorted([i+1, j+1])

            # populate hash table
            hash_table[n].append(i)

### TEST CODE ###

s = Solution()

test_cases = [
    # ([0,1], ([1,1,2], 2)),
    ([1,2], ([2,7,11,15], 9)),
    ([2,3], ([3,2,4], 6)),
    ([3,5], ([3,1,4,2,7,5], 11)),
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
