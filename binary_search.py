from typing import Union


def binarysearch(value: Union[int,str], valist:list) -> Union[int, None]:
    """
    Binary Search algorithm's implementation. The list passed as an argument must be previously sorted.
    """
    floor = 0
    roof = len(valist) - 1
    its = 0

    while floor <= roof:

        its +=1
        mid = (floor + roof) // 2

        if valist[mid] == value:

            return mid, its

        elif valist[mid] > value:

            roof = mid - 1

        elif valist[mid] < value:

            floor = mid + 1

    return None, its


if __name__ == '__main__':

    from random import randint

    threshold = 300
    ntarget = randint(0,threshold)
    ntest = sorted(list(set([randint(0,threshold) for _ in range(0,threshold)])))

    print('target: ', ntarget)
    print('list:', ntest)
    ind, iterations = binarysearch(ntarget,ntest)

    if ind is not None:
        print('{0} in {1} iterations'.format(ntest[ind]==ntarget, iterations))
    else:
        print('{0} in {1} iterations'.format(None,iterations))

