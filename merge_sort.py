

def mergesort(vlist:list, minchunk:int = 2) -> list:

    """
        Approximation to merge sort algorithm.
    """

    def sortchunck(mlist:list) -> list:

        ops = -1
        while ops != 0:

            ops =0
            for j in range(len(mlist)-1,0,-1):

                if mlist[j] < mlist[j-1]:

                    mlist[j], mlist[j-1] = mlist[j-1], mlist[j]

                    ops += 1

        return mlist

    list_length = len(vlist)

    if minchunk >= list_length:

        return sortchunck(vlist)

    else:

        n_list = []
        for i in range(0,list_length,minchunk):

            n_list += sortchunck(vlist[i:i+minchunk])

        return mergesort(n_list,minchunk**2)


if __name__ == '__main__':

    from random import randint

    threshold = 10
    testlist = [randint(0,threshold) for _ in range(0,threshold)]
    sorted_list = mergesort(testlist)

    print('original:', testlist)
    print('sorted:', sorted_list)

    from collections import Counter
    #I use Counter class to check whether or not both list contain the same values with the same frequencies
    print(Counter(testlist)==Counter(sorted_list))
