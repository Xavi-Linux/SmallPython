
"""

Divide and conquer approach on very basic stuff

"""


def sumlist(target_list: list) -> int:

    if len(target_list) == 1:

        return target_list[0]

    else:

        return target_list[0] + sumlist(target_list[1:])


def countlist(target_list: list) -> int:

    if not target_list:

        return 0

    else:

        return 1 + countlist(target_list[1:])


def maxnum(target_list: list) -> int:

    floor = 0
    roof = countlist(target_list) - 1
    mid = (floor + roof) //2

    if roof == 1:

        return target_list[0] if target_list[0] >= target_list[1] else target_list[1]

    elif roof == 0:

        return target_list[0]

    else:

        return maxnum([maxnum(target_list[floor:mid]), maxnum(target_list[mid:])])


if __name__ == '__main__':

    from random import randint

    threshold = 100
    testlist = [randint(0,threshold) for _ in range(0,20)]

    print(testlist)
    print('Max number:', maxnum(testlist))

    # I compare my function's result to python's built-in:
    print(maxnum(testlist) == max(testlist))

    for i in range(5,11):

        print(sumlist(testlist), countlist(testlist))
        testlist.append(i)
