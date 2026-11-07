def second_largest(nums: list[int]) -> int:
    """Return the second largest different value, or -1."""
    # TODO: write your solution here
    if len(nums) == 1 or len(nums) == 0:
        return -1
    largest = max(nums)
    second_largest_num = -1
    for i in nums:
        if i < largest and i > second_largest_num:
            second_largest_num = i
    return second_largest_num
