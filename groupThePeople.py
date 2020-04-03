def groupThePeople(groupSizes):
    size_dict = {}
    result = []
    index = 0
    for size in groupSizes:
        if size in size_dict.keys():
            size_dict[size].append(index)
        else:
            size_dict[size] = [index]
        index += 1

    for key in size_dict.keys():
        temp = size_dict[key]
        if len(size_dict[key]) == key:
            result.append(temp)
        else:
            for step in range(len(temp) // key):
                result.append(temp[step * key: (step + 1) * key])

    return result


if __name__ == '__main__':
    groupThePeople([3, 3, 3, 3, 3, 1, 3])
