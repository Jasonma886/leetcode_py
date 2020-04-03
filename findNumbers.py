def findNumbers(nums):
    if len(nums) == 0:
        return 0
    counter = 0
    for num in nums:
        num_len = len(str(num))
        if num_len % 2 == 0:
            counter += 1
    return counter

if __name__ == '__main__':
    print(findNumbers([12,345,2,6,7896]))