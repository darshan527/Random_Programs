"""Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space."""
def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    xor = 0
    for num in nums:
        xor = xor ^ num
    # Find the rightmost set bit
    rightmost_set_bit = xor & ~(xor - 1)
    # Get the numbers based on the rightmost set bit
    a = 0
    b = 0
    for num in nums:
        if num & rightmost_set_bit:
            a = a ^ num
        else:
            b = b ^ num
    return [a, b]