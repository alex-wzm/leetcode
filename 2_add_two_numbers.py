# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def __repr__(self):
        return f"{self.val} {f'-> {self.next}' if self.next is not None else ''}"

class Solution: # Accepted
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        NOTE: Representing input numbers as int[] and str allows us to 
            conveniently type-cast in order to take advantage of
            Pythonic syntactic sugar to execute addition operation.
        """

        # init list to represent numbers extracted from linked list
        int1, int2 = [], []
        
        # extract numbers from linked lists
        while True:
            int1.append(l1.val)
            if l1.next is None:
                break
            l1 = l1.next

        while True:
            int2.append(l2.val)
            if l2.next is None:
                break
            l2 = l2.next

        # init strings to represent numbers
        str1, str2 = '', ''

        # compile number as string
        for i in int1[::-1]:
            str1 += str(i)

        for i in int2[::-1]:
            str2 += str(i)

        # compute result by casting str representations to int
        ans = int(str1) + int(str2)

        # init ouput as None because final ListNode.next must == None
        # according to given ListNode definition
        output = None

        # iteratively construct output as linked list ListNode
        for i in str(ans):
            new_node = ListNode(i)
            new_node.next = output
            output = new_node

        return output
        

### TEST CODE ###

s = Solution()

test_cases = [
    (ListNode(7, ListNode(0, ListNode(8))),
            (ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))))),
]

count_passes = 0

for expected_output, input in test_cases:
    print("="*50)
    print(f"INPUT: ({input[0]}) + ({input[1]})")

    output = s.addTwoNumbers(input[0], input[1])

    print(f"OUTPUT: {output}")
    print(f"EXPECTED: {expected_output}\n")
    
    if output == expected_output: # TODO
        print("PASS")
        count_passes += 1
    else:
        print("FAIL")

print("="*50)
print(f"Passed {count_passes}/{len(test_cases)} test cases.\n")
