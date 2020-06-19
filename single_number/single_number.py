'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    counts = {}

    for num in arr:
        if num in counts:
            del counts[num]
        else:
            counts[num] = 1

    for k, v in counts.items():
        if v == 1:
            return k


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")


# def single_number(nums):
#     # keep track of number of times an item occurs in input
#     counts = {}
#     # loop through input list 0(n)
#     for num in nums:
#         # if item in counts
#         if num in counts:
#             # remove item
#             del counts[num]
#         # otherwise
#         else:
#             counts[num] = 1
#             # add item
#     for k, v in counts.items():  # 0(n)
#         if v == 1:
#             return k
