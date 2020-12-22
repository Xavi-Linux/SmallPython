from typing import Union


class MyQueue:

    def __init__(self):

        self.__queue = []

    def queuelength(self) -> int:

        return len(self.__queue)

    def retrievequeue(self):

        return self.__queue

    def enqueue(self, *items):

        for item in items:

            if hasattr(item, '__iter__'):

                self.__queue.extend(item)

            else:

                self.__queue.append(item)

    def dequeue(self):

        return self.__queue.pop(0)

    def isempty(self) -> bool:

        return self.queuelength() == 0


class MyBreadthSearch:

    def __init__(self, dictmap: dict):

        self.graph = dictmap

    def __buildtracechain(self, start_point, end_point, trace: list) -> str:

        for i in range(len(trace)-1,-1,-1):

            if trace[i][-1] == end_point:

                if trace[i] == start_point + '-' + end_point:

                    return start_point + '-' + end_point

                else:

                    return self.__buildtracechain(start_point,trace[i][0],trace[:i]) + trace[i][1:]

    def findpath(self, start_point, end_point) ->Union[str, None]:

        if start_point not in self.graph:

            return 'Start point does not exist!'

        else:

            queue = MyQueue()

            checked: list = []

            tracer: list = [start_point + '-' + el for el in self.graph[start_point]]

            queue.enqueue(self.graph[start_point])

            while not queue.isempty():

                value = queue.dequeue()

                if value in checked:
                    continue

                if value == end_point:

                    return self.__buildtracechain(start_point, value, tracer)

                else:

                    if self.graph.get(value):

                        tracer.extend([value + '-' + el for el in self.graph.get(value)])

                    queue.enqueue(self.graph.get(value))
                    checked.append(value)
            return None


if __name__ == '__main__':

    graph_1 = {'A':['B','C'],
             'B': ['D'],
             'C': ['D'],
             'D': ['F','G'],
             'E': ['C']
             }

    graph_2 = {'A':['B'],
               'B':['D','E'],
               'C':['D']}

    graph_3 = {'A':['B','C','D'],
               'B':['K'],
               'C':['J', 'I'],
               'D':['E', 'F'],
               'K':['R'],
               'J':['K'],
               'I':['L'],
               'E':['H'],
               'F':['G'],
               'R':['M'],
               'L':['M'],
               'G':['H'],
               'M':['N'],
               'H':['O'],
               'N':['O']
               }

    bread_search = MyBreadthSearch(graph_3)

    print(bread_search.findpath('A', 'O'))

