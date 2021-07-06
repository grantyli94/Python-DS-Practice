def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    counts = {}
    max_count = 0
    mode = 0
    for num in nums:
        counts[num] = counts.get(num,0) + 1
    for num in counts.keys():
        if counts[num] > max_count:
            max_count = counts[num]
            mode = num
    return mode



    # unique_nums = set(nums)
    # count = 0
    # mode = 0
    # for num in unique_nums:
    #     if nums.count(num) > count:
    #         count = nums.count(num)
    #         mode = num
    # return mode

    # refactor for O(n)