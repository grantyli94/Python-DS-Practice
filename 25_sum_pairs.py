def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    seen = set()
    counts = set(nums)
    # pairs = []

    for num in nums:
        if goal - num in counts:
            seen.add(goal - num)
        if num in seen:
            return (goal - num, num)

    return ()

    # for num in nums:
    #     if goal - num in counts:
    #         pairs.append([num, goal-num])
    #         counts.remove(num)
    # if not pairs:
    #     return ()

    # lowest_idx = len(nums)
    # idx = 0

    # for i in range(len(pairs)):
    #     if nums.index(pairs[i][1]) < lowest_idx: 
    #         lowest_idx = nums.index(pairs[i][1])
    #         idx = i 
            

    # return tuple(pairs[idx])