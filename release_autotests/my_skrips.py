
if __name__ == "__main__":
    # nums = [1,3,5,6]
    # target = 7
    #
    # try:
    #     print(nums.index(target))
    # except ValueError:
    #     for index, value in enumerate(nums):
    #         if value > target:
    #             print(index)
    #             break
    #     print(len(nums))


    # try:
    #     return nums.index(target)
    # except ValueError:
    #     min_num, max_num = min(nums), max(nums)
    #     if target < min_num:
    #         return 0
    #     if target > max_num:
    #         return len(nums)
    #     middle_index = (len(nums) - 1) // 2
    #     is_left_min, is_right_max = False, False
    #     while not is_left_min or not is_right_max:
    #         left, right = nums[middle_index], nums[middle_index + 1]
    #         is_left_min, is_right_max = left < target, target < right
    #         if not is_left_min:
    #             middle_index -= 1
    #         elif not is_right_max:
    #             middle_index += 1
    #     return middle_index + 1




    # nums = [1,1,2,4,9]
    # k = 9

    # print(sum(n < k for n in nums))

    # if max(nums) < k:
    #     print(len(nums))
    #
    # idx = 0
    #
    # for idx, value in enumerate(sorted(nums)):
    #     if value >= k:
    #         break
    # print(idx)

    # import math
    # l1 = [2,4,3]
    # l2 = [5,6,4]
    #
    # l1 = [str(i) for i in l1]
    # l2 = [str(i) for i in l2]
    # num1 = int("".join(l1))
    # num2 = int("".join(l2))
    # str_ = str(num1 + num2)
    # lst_s = [int(i) for i in str_]
    # print(lst_s[::-1])
    #
    # print(
    #     (lambda num: [(num // (10**i)) % 10 for i in range(1 if not num else int(math.log10(num)) + 1)])
    #     (sum(n * 10**i for i, n in enumerate(l1[::-1])) + sum(n * 10**i for i, n in enumerate(l2[::-1])))
    # )

    # a = "11"
    # b = "1"
    # binary1, binary2 = int(a, 2), int(b, 2)
    # while binary2:
    #     result = binary1 ^ binary2
    #     carry = (binary1 & binary2) << 1
    #     binary1, binary2 = result, carry
    # print(bin(binary1)[2:])

    # num1 = "2"
    # num2 = "3"
    # if num1 == "0" or num2 == "0":
    #     print("0")
    #
    # m, n = len(num1), len(num2)
    # # Initialize an array to store the result of multiplication.
    # # The maximum length of the product can be m + n.
    # result = [0] * (m + n)
    #
    # # Iterate through num1 from right to left
    # for i in range(m - 1, -1, -1):
    #     # Iterate through num2 from right to left
    #     for j in range(n - 1, -1, -1):
    #         # Convert characters to integers
    #         digit1 = int(num1[i])
    #         digit2 = int(num2[j])
    #
    #         # Calculate the product of the current digits
    #         product = digit1 * digit2
    #
    #         # Determine the positions in the result array
    #         # p1 is for the tens place, p2 is for the ones place
    #         p1 = i + j
    #         p2 = i + j + 1
    #
    #         # Add the product to the corresponding positions in the result array
    #         # Handle carry-over
    #         total_sum = product + result[p2]
    #         result[p2] = total_sum % 10  # Store the unit digit
    #         result[p1] += total_sum // 10  # Add the carry to the tens place
    #
    # # Convert the result array to a string
    # # Find the first non-zero digit to handle leading zeros
    # start_index = 0
    # while start_index < len(result) - 1 and result[start_index] == 0:
    #     start_index += 1
    #
    # # Join the digits from the start_index to form the final string
    # print("".join(map(str, result[start_index:])))

    # sentence = "1 2 $3 4 $5 $6 7 8$ $9 $10$"
    # discount = 100
    #
    # result_words = []
    #
    # for word in sentence.split():
    #     if len(word) > 1 and word[0] == "$" and word[1:].isdigit():
    #         price = int(word[1:])
    #         disc = 1 - discount / 100
    #         disc_price = price * disc
    #         word = f"${disc_price:.2f}"
    #     result_words.append(word)
    # print(" ".join(result_words))

    # product = ["Cashier", "getBill", "getBill", "getBill", "getBill", "getBill", "getBill", "getBill"]
    # amount = [
    #     [3, 50, [1, 2, 3, 4, 5, 6, 7], [100, 200, 300, 400, 300, 200, 100]],
    #     [[1, 2], [1, 2]],
    #     [[3, 7], [10, 10]],
    #     [[1, 2, 3, 4, 5, 6, 7], [1, 1, 1, 1, 1, 1, 1]],
    #     [[4], [10]],
    #     [[7, 3], [10, 10]],
    #     [[7, 5, 3, 1, 6, 4, 2], [10, 10, 10, 9, 9, 9, 7]],
    #     [[2, 3, 5], [5, 3, 2]],
    # ]
    #
    # from typing import List
    #
    # class Cashier:
    #     def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
    #         self.customer_count = 0
    #         self.n = n
    #         self.discount = discount
    #         self.product_price_map = {product_id: price
    #                                   for product_id, price in zip(products, prices, strict=False)}
    #
    #     def getBill(self, product: List[int], amount: List[int]) -> float:
    #         self.customer_count += 1
    #         discount_percentage = self.discount if self.customer_count % self.n == 0 else 0
    #         total_bill = 0.0
    #         for product_id, quantity in zip(product, amount, strict=False):
    #             subtotal = self.product_price_map[product_id] * quantity
    #             total_bill += subtotal - (discount_percentage * subtotal) / 100
    #
    #         return total_bill
    #
    #
    # print(a)

    # nums1 = [1,2]
    # nums2 = [3,4]
    #
    # result_nums = sorted(nums1 + nums2)
    # length = len(result_nums)
    # if length % 2:
    #     print(result_nums[length // 2])
    # else:
    #     print((result_nums[length // 2 - 1] + result_nums[length // 2]) / 2)


    # s = "PAYPALISHIRING"
    # numRows = 3
    #
    # if numRows == 1 or numRows >= len(s):
    #     print(s)
    #
    # rows = [[] for _ in range(numRows)]
    #
    # current_row = 0
    # direction = 1
    #
    # for char in s:
    #     rows[current_row].append(char)
    #
    #     if current_row == 0:
    #         direction = 1
    #     elif current_row == numRows - 1:
    #         direction = -1
    #
    #     current_row += direction
    #
    # result = "".join(["".join(row) for row in rows])
    # print(result)


    s = "aa"
    p = "a"

    # m = len(s)
    # n = len(p)
    # dp = [[False] * (n + 1) for _ in range(m + 1)]
    # dp[0][0] = True
    #
    # def isMatch(i: int, j: int) -> bool:
    #     return (j >= 0 and p[j] == ".") or s[i] == p[j]
    #
    # for j, c in enumerate(p):
    #     if c == "*" and dp[0][j - 1]:
    #         dp[0][j + 1] = True
    #
    # for i in range(m):
    #     for j in range(n):
    #         if p[j] == "*":
    #             noRepeat = dp[i + 1][j - 1]
    #             doRepeat = isMatch(i, j - 1) and dp[i][j + 1]
    #             dp[i + 1][j + 1] = noRepeat or doRepeat
    #         elif isMatch(i, j):
    #             dp[i + 1][j + 1] = dp[i][j]
    #
    # print(dp[m][n])

    # from functools import cache
    #
    # s_length = len(s)
    # p_length = len(p)
    #
    # @cache
    # def match_helper(s_index: int, p_index: int) -> bool:
    #
    #     if p_index >= p_length:
    #         print( s_index == s_length)
    #
    #     if p_index + 1 < p_length and p[p_index + 1] == "*":
    #         skip_pattern = match_helper(s_index, p_index + 2)
    #
    #         match_current = (
    #             s_index < s_length
    #             and (s[s_index] == p[p_index] or p[p_index] == ".")
    #             and match_helper(s_index + 1, p_index)
    #         )
    #
    #         print((skip_pattern or match_current))
    #
    #     print((
    #         s_index < s_length
    #         and (s[s_index] == p[p_index] or p[p_index] == ".")
    #         and match_helper(s_index + 1, p_index + 1)
    #     ))
    #
    # print(match_helper(0, 0))


    # import re
    #
    # result = re.findall(p, s)
    #
    # print(len(result) > 0 and len(result[0]) == len(s))

    # nums = [-1, 0, 1, 2, -1, -4]
    # nums.sort()
    # result = []
    # n = len(nums)
    #
    # for i in range(n):
    #     if i > 0 and nums[i] == nums[i - 1]:
    #         continue
    #
    #     left = i + 1
    #     right = n - 1
    #
    #     while left < right:
    #         sum = nums[i] + nums[left] + nums[right]
    #
    #         if sum == 0:
    #             result.append([nums[i], nums[left], nums[right]])
    #
    #             while left < right and nums[left] == nums[left + 1]:
    #                 left += 1
    #             while left < right and nums[right] == nums[right - 1]:
    #                 right -= 1
    #
    #             left += 1
    #             right -= 1
    #         elif sum > 0:
    #             right -= 1
    #         else:
    #             left += 1
    #
    # print(result)


    # digits = "23"
    # # ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    #
    # sym = [
    #     "abc",
    #     "def",
    #     "ghi",
    #     "jkl",
    #     "mno",
    #     "pqrs",
    #     "tuv",
    #     "wxyz"
    # ]
    # result = [""]
    #
    # if not digits:
    #     print([])
    #
    # for digit in digits:
    #     letters = sym[int(digit) - 2]
    #     # for existing in result.copy():
    #     #     result.pop(0)
    #     #     for letter in letters:
    #     #         print(letter)
    #     #         result.append(existing + letter)
    #     result = [existing + letter
    #               for existing in result
    #               for letter in letters]
    #
    # # print([i for i in result if len(i) == len(digits)])
    # print(result)


    # head = [1,2,3,4,5]
    # n = 2
    # head = head[::-1]
    # head.pop(2 -1 )
    # head = head[::-1]
    # print(head)

    # nums = [0,0,1,1,1,2,2,3,3,4]
    # result = []
    # for num in nums:
    #     if num not in result:
    #         result.append(num)
    # print(len(result))
    #
    #
    # write_index = 0
    # for current_num in nums:
    #     if write_index == 0 or current_num != nums[write_index - 1]:
    #         nums[write_index] = current_num
    #         write_index += 1
    # print(write_index)

    # nums = [0,1,2,2,3,0,4,2]
    # val = 2
    # k = 0
    # for i in range(len(nums)):
    #     if nums[i] != val:
    #         nums[k] = nums[i]
    #         k += 1
    # print(k)


    # nums = [-1,2,1,-4]
    # target = 1
    # nums.sort()
    # n = len(nums)
    # closest_sum = float("inf")
    #
    # for i in range(n):
    #     left = i + 1
    #     right = n - 1
    #     while left < right:
    #         sum = nums[i] + nums[left] + nums[right]
    #
    #         if sum == target:
    #             print(sum)
    #
    #         if abs(sum - target) < abs(closest_sum - target):
    #             closest_sum = sum
    #
    #         if sum > target:
    #             right -= 1
    #         else:
    #             left += 1
    # print(closest_sum)

    # nums = [1,0,-1,0,-2,2]
    # target = 0
    # nums.sort()
    # n = len(nums)
    # result = []
    #
    # for i in range(n):
    #     if i > 0 and nums[i] == nums[i - 1]:
    #         continue
    #
    #     for j in range(i + 1, n):
    #         if j > i + 1 and nums[j] == nums[j - 1]:
    #             continue
    #
    #         left = j + 1
    #         right = n - 1
    #
    #         while left < right:
    #             sum = nums[i] + nums[j] + nums[left] + nums[right]
    #             if sum < target:
    #                 left += 1
    #             elif sum > target:
    #                 right -= 1
    #             else:
    #                 result.append([nums[i], nums[j], nums[left], nums[right]])
    #                 left += 1
    #                 right -= 1
    #
    #                 while left < right and nums[left] == nums[left - 1]:
    #                     left += 1
    #
    #                 while left < right and nums[right] == nums[right + 1]:
    #                     right -= 1
    # print(result)


    # nums = [5,7,7,8,8,10]
    # target = 8
    #
    # # left_index = bisect_left(nums, target)
    # #
    # # right_index = bisect_left(nums, target + 1)
    # #
    # # if left_index == right_index:
    # #     print([-1, -1])
    # # else:
    # #     print([left_index, right_index - 1])
    #
    # try:
    #     first_index = nums.index(target)
    # except ValueError:
    #     print([-1, -1])
    #
    # last_index = len(nums) - 1 - nums[::-1].index(target)
    # print([first_index, last_index])


    # x = 4
    # out = 2
    #
    # root = math.sqrt(x)
    # print(int(root))
    #
    # left, right = 0, x
    #
    # while left < right:
    #
    #     mid = (left + right + 1) >> 1
    #
    #     if mid > x // mid:
    #         right = mid - 1
    #     else:
    #         left = mid
    #
    # print(left)


    # path = "/home//foo/"
    # directory_stack = []
    # path_com = path.split("/")
    #
    # for com in path_com:
    #     if com == "." or not com:
    #         continue
    #
    #     if com == "..":
    #         if directory_stack:
    #             directory_stack.pop()
    #     else:
    #         directory_stack.append(com)
    #
    # path_res = f"/{'/'.join(directory_stack)}"
    #
    # print(path_res)
    # nums1 = [1,2,3,0,0,0]
    # m = 3
    # nums2 = [2,5,6]
    # n = 3
    #
    # for i in range(len(nums2)):
    #     nums1[-i -1] = nums2[i]
    # nums1.sort()
    # print(nums1)






    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    #
    # class Solution:
    #     def hasPathSum(self, root: Optional[TreeNode], targetSum: int):
    #         def sum(a: Optional[TreeNode], cur_sum: int):
    #             if a is None:
    #                 return False
    #
    #             cur_sum += a.val
    #             if a.left is None and a.right is None:
    #                 return cur_sum == targetSum
    #
    #             return sum(a.left, cur_sum) or sum(a.right, cur_sum)
    #         return sum(root, 0)
    #
    # a = Solution()
    # root = TreeNode(
    #     val=5,
    #     left=TreeNode(
    #         val=4,
    #         left=TreeNode(
    #             val=11,
    #             left=TreeNode(
    #                 val=7,
    #             ),
    #             right=TreeNode(val=2)
    #         ),
    #     ),
    #     right=TreeNode(
    #         val=8,
    #         left=TreeNode(
    #             val=13,
    #         ),
    #         right=TreeNode(
    #             val=4,
    #             right=TreeNode(
    #                 val=1,
    #             )
    #         )
    #     )
    # )
    # print(a.hasPathSum(root = root, targetSum = 22))



    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    #
    # class Solution:
    #     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    #         dummy_head = ListNode()
    #         carry = 0
    #         current_node = dummy_head
    #
    #         while l1 or l2 or carry:
    #             digit1 = l1.val if l1 else 0
    #             digit2 = l2.val if l2 else 0
    #
    #             total_sum = digit1 + digit2 + carry
    #
    #             carry, digit_value = divmod(total_sum, 10)
    #
    #             current_node.next = ListNode(digit_value)
    #             current_node = current_node.next
    #
    #             l1 = l1.next if l1 else None
    #             l2 = l2.next if l2 else None
    #
    #         return dummy_head.next
    #
    #
    # l1 = ListNode(
    #     val=2,
    #     next=(ListNode(
    #         val=2,
    #         next=(ListNode(val=3))
    #     ))
    # )
    # l2 = ListNode(
    #     val=5,
    #     next=(ListNode(
    #         val=6,
    #         next=(ListNode(
    #             val=4
    #         ))
    #     ))
    # )
    #
    # a = Solution()
    # print(a.addTwoNumbers(l1, l2))



    # s = "pwwkew"
    # out = 3
    # from collections import Counter
    #
    # char_count = Counter()
    #
    # max_length = 0
    # left = 0
    #
    # for right, char in enumerate(s):
    #     char_count[char] += 1
    #
    #     while char_count[char] > 1:
    #         char_count[s[left]] -= 1
    #         left += 1
    #
    #     max_length = max(max_length, right - left + 1)
    #
    # print(max_length)


    # nums1 = [1,2,2,1]
    # nums2 = [2,2]
    #
    # print(list(set(nums1).intersection(set(nums2))))

    # symb = {
    #     "I": 1,
    #     "V": 5,
    #     "X": 10,
    #     "L": 50,
    #     "C": 100,
    #     "D": 500,
    #     "M": 1000
    # }
    # s = "MCMXCIV"
    # from itertools import pairwise
    # res = sum((-1 if symb[i] < symb[next_i] else 1) * symb[i] for i, next_i in pairwise(s))
    # res += symb[s[-1]]
    # print(res)

    # strs = ["flower", "flow", "flight"]
    #
    # if not strs:
    #     print("")
    #
    # for i in range(len(strs[0])):
    #     for string in strs[1:]:
    #         if len(string) <= i or string[i] != strs[0][i]:
    #             print(strs[0][:i])
    # print(strs[0])

    # s = "([)]"
    # stack = []
    # valid_pairs = {"()", "[]", "{}"}
    # for c in s:
    #     if c in "([{":
    #         stack.append(c)
    #     else:
    #         if not stack or stack.pop() + c not in valid_pairs:
    #             print(False)
    #
    # print(not stack)
    # s = "Hello World"
    # s = s.strip()
    # s = s.split()
    # print(len(s[-1]))

    # nums = [2, 7, 15, 11]
    # target = 18
    #
    # def two_sum(nums, target):
    #     num_map = {}
    #
    #     for idx, num in enumerate(nums):
    #         compl = target - num
    #         if compl in num_map:
    #             return [num_map[compl], num]
    #         num_map[num] = num
    #
    #     return []
    #
    # print(two_sum(nums, target))

    # def fibonacci():
    #     a, b = 0, 1
    #     while True:
    #         yield a
    #         a, b = b, a + b
    #
    # # Пример использования:
    # for num in fibonacci():
    #     print(num)
    #     if num > 100:
    #         break


    board =[["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

    # def sudoku(board):
    #     rows = defaultdict(set)
    #     cols = defaultdict(set)
    #     squares = defaultdict(set)
    #
    #     for r in range(9):
    #         for c in range(9):
    #             if board[r][c] == ".":
    #                 continue
    #
    #             val = board[r][c]
    #             if val in rows[r] or val in cols[c] or val in squares[(r // 3, c // 3)]:
    #                 return False
    #
    #             rows[r].add(val)
    #             cols[c].add(val)
    #             squares[(r // 3, c // 3)].add(val)
    #
    #     return True
    #
    # sudoku(board)

    # n = 3
    # result = []
    # def backtrack(current_string, open_count, close_count):
    #     if len(current_string) == 2 * n:
    #         result.append(current_string)
    #         return
    #
    #     if open_count < n:
    #         backtrack(current_string + "(", open_count + 1, close_count)
    #
    #     if close_count < open_count:
    #         backtrack(current_string + ")", open_count, close_count + 1)
    #
    # backtrack("", 0, 0)
    # print(result)
