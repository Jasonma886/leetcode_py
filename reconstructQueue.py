# def reconstructQueue(people):
#     print(people)
#     s_people = sorted(people)
#     for person in s_people:
#         index = person[-1]
#         old_index = people.index(person)
#
#
#     shortest = min(people)
#     old_index = people.index(shortest)
#     new_index = shortest[-1]

def rule(x):
    return lambda x: (-x[0], x[1])


def reconstructQueue(people):
    # people = sorted(people, key=lambda x: (-x[0], x[1]))
    people = sorted(people, key=lambda x: (-x[0], x[1]))
    print(people)
    res = []
    for p in people:
        res.insert(p[1], p)
    return res


if __name__ == '__main__':
    print(reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
