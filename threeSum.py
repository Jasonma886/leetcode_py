# 15. 3Sum

def threeSum(nums):
    """
     :type nums: List[int]
     :rtype: List[List[int]]
     """
    result = []
    while len(nums):
        first = nums.pop()
        second_nums = nums[:]
        while len(second_nums):
            second = second_nums.pop()
            third_nums = second_nums[:]
            while len(third_nums):
                third = third_nums.pop()
                if first + second + third == 0:
                    print(first, second, third)
                    result.append([first, second, third])

    return result


if __name__ == '__main__':
    threeSum([-1, 0, 1, 2, -1, -4])

##                               _
##  _._ _..._ .-',     _.._(`))
## '-. `     '  /-._.-'    ',/
##    )         \            '.
##   / _    _    |             \
##  |  a    a    /              |
##  \   .-.                     ;
##   '-('' ).-'       ,'       ;
##      '-;           |      .'
##         \           \    /
##         | 7  .__  _.-\   \
##         | |  |  ``/  /`  /
##        /,_|  |   /,_/   /
##           /,_/      '`-'
##
