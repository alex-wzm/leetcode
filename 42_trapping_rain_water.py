from typing import List

class MySolution1(object): # WRONG
    def trap(self, height: List[int]) -> int:
        """
        :type height: List[int]
        :rtype: int
        """

        print(f"### processing {height}")
        
        water = 0
        latest_end = 0
        
        for i in range(0, len(height)-1):
            if(i < latest_end):
                print(f"skipping i: {i}")
                continue
            print(f"computing i: {i}")
            volume = 0
            is_increasing = False
            for j in range(i+1, len(height)):
                if height[j] < height[i]:
                    volume += (height[i]-height[j])
                    # print(f"potential volume so far: {volume}")
                if height[j] >= height[i]:
                    print(f"j height[{j}]:{height[j]} >= height[{i}]:{height[i]}")
                    print(f"volume from {i} to {j} is {volume}")
                    water += volume
                    print(f"total water is {water}")
                    latest_end = j
                    break

                if height[j] > height[j-1]:
                    is_increasing = True
                elif height[j] < height[j-1]:
                    is_increasing = False

                if j == len(height)-1 and is_increasing:
                    print(f"end of list: height[{i}]:{height[i]}, height[{j}]:{height[j]}")
                    reversed_sublist = height[i:j+1]
                    reversed_sublist.reverse()
                    water += self.trap(reversed_sublist)
                    latest_end = j
                    break

                if not j == len(height)-1 and height[j] > height[j+1] and is_increasing:
                    print(f"end of trough: height[{i}]:{height[i]}, height[{j}]:{height[j]}")
                    reversed_sublist = height[i:j+1]
                    reversed_sublist.reverse()
                    water += self.trap(reversed_sublist)
                    latest_end = j
                    break
        
        return water

class MySolution2(object): # WRONG
    def trap(self, height: List[int]) -> int:
        """
        :type height: List[int]
        :rtype: int
        """
        
        water = 0
        latest_end = 0

        for i, h1 in enumerate(height):
            if(i < latest_end):
                print(f"skipping i: {i}")
                continue
            print(f"computing i: {i}")
            if h1 > 0:
                largest_so_far, largest_so_far_index = 0, -1 # in case there's no j s.t. height[j] >= height[i]
                for j, h2 in enumerate(height[i+1:-1]):
                    if h2 >= largest_so_far:
                        largest_so_far = h2
                        largest_so_far_index = j
                    if h2 >= h1:
                        print(f"============ height[{i+j+1}]:{h2} >= height[{i}]:{h1} ============")
                        volume = self.sum_volume(height, i, h1, i+j+1, h2)
                        print(f"volume: {volume}") # sum volume between h1 and h2
                        water += volume
                        latest_end = i+j+1
                        break

        return water

    def sum_volume(self, height, i, h1, j, h2):
        smaller = min(h1, h2)
        volume = 0

        # TODO: check if there's a trough for water to collect
        #       i.e. height must first decrease then increase
        #       AND height cannot be strictly descrings or increasing

        for idx in range(i+1, j):
            volume += smaller - height[idx]

        return volume

class Solution1(object): # LeetCode Approach 1: Brute force (Time Limit Exceeded)
    def trap(self, height: List[int]) -> int:
        """
        :type height: List[int]
        :rtype: int
        """

        water = 0
        
        for i in range(len(height)):
            max_left, max_right = height[0], height[-1]

            for j in range(i,0,-1):
                max_left = max(max_left, height[j])
            
            for j in range(i,len(height)):
                max_right = max(max_right, height[j])

            water += min(max_left, max_right) - height[i]

        return water
        """
        Analysis:
        - Time: O(n^2)
        - Space: O(1)
        """

class Solution2(object): # LeetCode Approach 2: Dynamic Programming (Accepted)
    def trap(self, height: List[int]) -> int:
        """
        :type height: List[int]
        :rtype: int
        """

        N = len(height)

        if height is None or N is 0:
            return 0
    
        water = 0

        # init stores for the heighest bounding bars from the left and right direction
        # fill with 0 (input is non-negative)
        left_max, right_max = [0]*N, [0]*N

        # init heights of first and last indices
        left_max[0] = height[0]
        right_max[N - 1] = height[N - 1]

        # storing max while iterating from left
        for i in range(1,N):
            left_max[i] = max(height[i], left_max[i - 1])

        # storing max while iterating from right
        for i in range(N-2,0,-1):
            right_max[i] = max(height[i], right_max[i + 1])

        # accumulate by summing difference between current and min of left and right bounds
        for i in range(1, N-1):
            water += min(left_max[i], right_max[i]) - height[i]

        return water
        """
        Analysis:
        - Time: O(n)
        - Space: O(n)
        """

class Solution3(object): # LeetCode Approach 3: Using stacks (Accepted)
    def trap(self, height: List[int]) -> int:
        """
        :type height: List[int]
        :rtype: int
        """

        water = 0

        # stack stores bounded bars that might enclose water
        stack = []

        for i in range(0, len(height)):
            while len(stack) > 0 and height[i] > height[stack[-1]]:
                """
                Entering this loop indicates the current index might store water.
                Storing water requires being bounded by two bars (one on each side).
                Hence, accumulating water requires len(stack) > 1.
                len(stack) = 1 indicates a slope that does not store water and we can discard accordingly
                """
                
                top = stack.pop()
                if len(stack) > 0:
                    distance = i-stack[-1]-1
                    bounded_height = min(height[i],height[stack[-1]]) - height[top]
                    water += distance*bounded_height

            stack.append(i)

        return water
        """
        Analysis:
        - Time: O(n)
        - Space: O(n)
        """

class Solution4(object): # LeetCode Approach 4: Using Two Pointers (Accepted)
    def trap(self, height: List[int]) -> int:
        """
        :type height: List[int]
        :rtype: int
        """

        N = len(height)

        if height is None or N is 0:
            return 0
    
        water = 0

        left, right = 0, N-1
        left_max, right_max = 0, 0

        """
        Starting from both ends of the array,
        increamentally accumulate bounded water
        by storing the max height from each direction and
        only accumulating when the height of the current (inner) bar
        is less than the height of the max (outer) bar
        for reach side respectively.
        """

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1

            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1

        return water
        """
        Analysis:
        - Time: O(n)
        - Space: O(1)
        """
        


### TEST CODE ###

s = Solution2()

test_cases = [
    (0, []),
    (6, [0,1,0,2,1,0,1,3,2,1,2,1]),
    (1, [4,2,3]),
    (1, [4,2,3,3]),
    (1, [5,4,1,2]),
    (1, [2,1,4,5]),
    (1, [4,9,4,5,3,2]),
    (94, [9,0,1,0,2,1,0,1,3,2,1,2,1,9]),
    (0, [9,8,7,6,5]),
    (0, [5,6,7,8,9]),
    (0, [1,1,1,1,1]),
    (0, [0]),
    (0, [0,0])
]

count_passes = 0

for expected_output, test in test_cases:
    print("="*50)
    print(f"INPUT: {test}")

    output = s.trap(test)

    print(f"OUTPUT: {output}")
    print(f"EXPECTED: {expected_output}\n")
    
    if output == expected_output:
        print("PASS")
        count_passes += 1
    else:
        print("FAIL")

print("="*50)
print(f"Passed {count_passes}/{len(test_cases)} test cases.\n")
