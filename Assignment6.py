# Question 1
# Give an algorithm to solve this problem.
# Determine the asymptotic time complexity of your algorithm, depending on the maximum n of the number of children
# and cookies. Give an argument as to why your algorithm is correct.
# https://leetcode.com/problems/assign-cookies/description/

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j, count = 0, 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1
        return count

# Time complexity: O(nlogn) where n is the maximum of the number of children and cookies.
# The algorithm sorts the children and cookies in ascending order and then iterates through the children and cookies.
# If the cookie size is greater than or equal to the child's greed factor, the child is satisfied. The algorithm returns
# the number of satisfied children. The algorithm is correct because it satisfies the children with the smallest greed
# factor first. This is accomplished by sorting the arrays before iterating through the arrays.

# Question 2
# Give an algorithm to solve this problem. Give an argument as to why your algorithm is correct.
# https://leetcode.com/problems/maximum-swap/description/

class Solution2:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        num_sorted = sorted(num, reverse=True)
        for i in range(len(num)):
            if num[i] != num_sorted[i]:
                j = len(num) - 1
                while num[j] != num_sorted[i]:
                    j -= 1
                num[i], num[j] = num[j], num[i]
                break
        return int(''.join(num))

# This algorithm sorts the digits of the number in descending order and then compares the digits of the original number
# with the sorted digits. If the digits are different, the algorithm swaps the digits to get the maximum number.
# The algorithm returns the maximum number after the swap. The algorithm is correct because it guarantees that the
# maximum number is obtained by swapping the digits.