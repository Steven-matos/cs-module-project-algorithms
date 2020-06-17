'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    # Your code here
    new_arr = []
    start = 0
    slide = k
    for i in range(len(nums)):
        high = float("-inf")
        for j in range(start, slide):
            if nums[j] > high:
                high = nums[j]
            if len(nums) < slide:
                return new_arr
        new_arr.append(high)
        start += 1
        slide += 1
    return new_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
