
def quicksort(vlist:list) -> list:
    """
        Quicksort implementation. Average case: O(n log n)
    """

    if len(vlist) <= 1:

        return vlist

    else:

        mid = (len(vlist) - 1) // 2

        pivot = vlist[mid]

        less = [v for v in vlist[:mid] + vlist[mid+1:] if v <= pivot]

        greater = [v for v in vlist[:mid] + vlist[mid+1:] if v > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == '__main__':

    from random import randint
    from collections import Counter

    threshold = 50
    testlist = [randint(0,threshold) for _ in range(0,threshold)]
    sorted_list = quicksort(testlist)
    print('original:', testlist)
    print('sorted:', sorted_list)

    # I use Counter class to check wether or not both list contain the same values with the same frequencies:
    print(Counter(testlist)==Counter(sorted_list))