
def selectionsort(vlist: list, ascending=True) -> list:

    """
        Selection sort implementation. O(n²)
    """

    sorted_list = []
    target_index = 0

    def findlargest(ulist: list) -> int:

        s_index = 0
        for i, v in enumerate(ulist):

            if i==0:
                s_index = i

            else:

                if v > ulist[s_index]:
                    s_index = i

        return s_index

    def findsmallest(ulist: list) -> int:

        s_index = 0
        for i, v in enumerate(ulist):

            if i == 0:
                s_index = i

            else:

                if v < ulist[s_index]:

                    s_index = i

        return s_index

    for _ in range(0, len(vlist)):

        if ascending:
            target_index = findsmallest(vlist)

        else:
            target_index = findlargest(vlist)

        sorted_list.append(vlist[target_index])
        vlist.pop(target_index)

    return sorted_list


if __name__ == '__main__':

    from random import randint
    from collections import Counter

    threshold = 100
    testlist = [randint(0,threshold) for _ in range(0,threshold)]
    sorted_list = selectionsort(testlist.copy(), False)

    print('Original: ', testlist)
    print('Sorted:', sorted_list)
    print('Same length: ', len(sorted_list)==len(testlist))

    # I use Counter class to check whether or not both lists contain the same values with the same frequencies.
    print(Counter(sorted_list)==Counter(testlist))


