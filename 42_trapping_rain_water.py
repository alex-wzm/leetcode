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
 
### TEST CODE ###

s = Solution1()

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
