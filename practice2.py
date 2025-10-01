# Q1. Write a Python program to flatten a nested list.

# stack = [1, [2, [3, 4], 5], 6]
#
# newstack=[]
#
# def flattern_stack(stack):
#     for ele in stack:
#         if isinstance(ele, list):
#             flattern_stack(ele)
#         else:
#             newstack.append(ele)
#
# flattern_stack(stack)
# print(newstack)


# Q2. Write a Python program to check if a string of brackets is balanced.

str = input()
pairs = {')': '(', '}': '{', ']': '['}
n = len(str)
stack = []
for i in range(n):
    if str[i] in "({[":
        stack.append(str[i])
    else:
        if not stack or pairs[str[i]]!=stack[-1]:
            print("Not balanced")
            exit()
        stack.pop()
else:
    if not stack:
        print("Balanced")
    else:
        print("Not balanced")
