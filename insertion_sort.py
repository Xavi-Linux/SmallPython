
def insertion_sort(ulist:list) -> list:

    for i in range(1, len(ulist)):

        pos = i - 1

        while pos >= 0:

            if ulist[pos] > ulist[pos+1]:

                ulist[pos+1],ulist[pos] = ulist[pos],ulist[pos+1]

            else:

                break

            pos -= 1

    return ulist


if __name__ == '__main__':

    from random import randint

    n = 10
    l = [randint(0,n) for _ in range(0,n)]

    print(insertion_sort(l))