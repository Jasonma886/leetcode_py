def numberOfSteps(x, count):
    if x == 0:
        return count
    count += 1
    if x % 2 == 0:
        x = x // 2
    else:
        x -= 1
    return numberOfSteps(x, count)


if __name__ == '__main__':
    print(numberOfSteps(23, 0))