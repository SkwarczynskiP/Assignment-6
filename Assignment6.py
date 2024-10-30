# Question 1
# Give an algorithm to solve this problem.
# Determine the asymptotic time complexity of your algorithm, depending on the maximum n of the number of children
# and cookies. Give an argument as to why your algorithm is correct.
# https://leetcode.com/problems/assign-cookies/description/

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort() # O(nlogn)
        s.sort() # O(nlogn)
        i, j = 0, 0
        while i < len(g) and j < len(s): # O(n)
            if g[i] <= s[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i

# Time complexity: O(nlogn) where n is the maximum of the number of children and cookies.
# The running time is due to the sorting of the greed factors and the sizes of the cookies O(nlgn). The while loop takes
# O(n) time to iterate through the children and cookies.
# The algorithm sorts both the greed factors of the children and the sizes of the cookies in ascending order.
# It then iterates through both lists, assigning the smallest available cookie that can satisfy each child's greed.
# This greedy approach ensures that the maximum number of children are satisfied because it always tries to satisfy the
# least greedy child first, leaving the larger cookies for the more greedy children.

# Question 2
# Give an algorithm to solve this problem. Give an argument as to why your algorithm is correct.
# https://leetcode.com/problems/maximum-swap/description/

class Solution2:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num)) # Convert the number to a list of digits
        num_sorted = sorted(num, reverse=True) # Sort the digits in descending order
        for i in range(len(num)): # Iterate through the digits of the number
            if num[i] != num_sorted[i]: # If the digit is different from the sorted digit
                j = len(num) - 1 #
                while num[j] != num_sorted[i]: # Find the index of the sorted digit
                    j -= 1
                num[i], num[j] = num[j], num[i]
                break
        return int(''.join(num)) # Convert the list of digits back to an integer

# This algorithm sorts the digits of the number in descending order and then compares the digits of the original number
# with the sorted digits to find the first position where they are different. It then swaps the digits with the largest
# possible digit to the left of the different digit. This ensures that the new number is greater than the original.
# The algorithm is correct because it always swaps the digits to the leftmost position possible to maximize the value
# of the number.