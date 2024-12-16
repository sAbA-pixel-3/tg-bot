# def is_uppercase(inp):
#     return inp.islower()
# print(is_uppercase("QW"))

# def balanced_num(number):
#     str_num = str(number)
#     length = len(str_num)
#     if length % 2 == 1:
#         middle_index = length // 2
#         left_sum = sum(int(digit) for digit in str_num[:middle_index])
#         right_sum = sum(int(digit) for digit in str_num[middle_index+1])
#     else:
#         middle_index = length // 2
#         left_sum = sum(int(digit) for digit in str_num[:middle_index-1])
#         right_sum = sum(int(digit) for digit in str_num[middle_index+1:])
#     if left_sum == right_sum:
#         return "Balanced"
#     else:
#         return "Not Balanced"
# print(balanced_num(557)) 



