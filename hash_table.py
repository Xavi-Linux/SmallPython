from math import cos


class MyHashTable:

    def __init__(self, initial_size):

        self.__array = [[None] for _ in range(0,initial_size)]

    def __loadfactor(self) -> float:

        return 1 - (self.__array.count([None])/len(self.__array))

    def __resize(self):

        self.__array = self.__array + [None] * len(self.__array)

    def __needsresizing(self) -> bool:

        if self.__loadfactor() > 0.7:

            return True

        else:

            return False

    def __hashfunction(self, key) -> int:

        l = len(self.__array) // 2

        return int(abs(cos(len(key)) * l) + abs(cos(ord(key[-1])) * l))

    def insert(self, key, value):

        if self.__needsresizing():

            self.__resize()

        k = self.__hashfunction(key)

        if not all(self.__array[k]):

            self.__array[k].pop(0)
            self.__array[k].append((key, value))

        else:

            if key in [element[0] for element in self.__array[k]]:

                raise Exception('Key already exists')

            else:

                self.__array[k].append((key, value))

    def read(self, key):

        k = self.__hashfunction(key)

        if self.__array[k][0] is None:

            return None

        for element in self.__array[k]:

            if key in element[0]:

                return element[1]

        return None

    def modify(self, key, new_value):

        k = self.__hashfunction(key)

        if self.__array[k][0] is None:

            raise Exception('Key doesn\'t exist')

        for element in self.__array[k]:

            if key in element[0]:

                element[1] = new_value

                break

        raise Exception('Key doesn\'t exist')

    def delete(self, key):

        k = self.__hashfunction(key)

        if self.__array[k][0] is None:

            return None

        for i,element in enumerate(self.__array[k]):

            if key in element[0]:

                self.__array[k].pop(i)

                if len(self.__array[k]) == 0:

                    self.__array[k].append(None)

        return None

    def __str__(self):

        return str(self.__array)


if __name__ == '__main__':

    c = MyHashTable(10)
    c.insert('Spain', 'Madrid')
    c.insert('Italy', 'Rome')
    c.insert('France', 'Paris')
    print(c)
    c.delete('Spain')
    print(c)
    c.insert('UK','London')
    print(c)
    print(c.read('France'))
    print(c.read('Italy'))


