class MyDijkstra:

    def __init__(self, graph_: dict):

        self.graph = graph_

        self.__costtable, self.__parenttable = self.__setuptables(self.graph.keys())

        self.end_point = self.__getendpoint()

    def __getendpoint(self):

        for k in self.graph:

            if not self.graph[k]:
                return k

    @staticmethod
    def __setuptables(keys):

        return {k:[float('inf'), False] for k in keys}, {k:'' for k in keys}

    @staticmethod
    def __findlowest(nodes: dict):

        if not nodes:
            return None

        min_value = float('inf')
        target_key = None
        for key, value in nodes.items():

            if value[0] < min_value and not value[1]:
                min_value = value[0]
                target_key = key

        return target_key

    @staticmethod
    def __updatetable(table: dict, new_values: dict, index=0):

        for value in new_values:

            if type(table[value]).__name__=='list':

                table[value][index] = new_values[value]

            else:

                table[value] = new_values[value]

    def __buildtracechain(self, table, end_point):

        if table[end_point]=='':

            return end_point

        else:

            parent = table[end_point]

            del table[end_point]

            return self.__buildtracechain(table, parent) + '-' + end_point

    def findpath(self, start_point):

        self.__costtable[start_point] = [0, True]

        self.__updatetable(self.__costtable, self.graph[start_point])

        self.__updatetable(self.__parenttable, {i:start_point for i in self.graph[start_point]})

        node = self.__findlowest(self.__costtable)

        while node is not None:

            neighbours = self.graph[node].keys()

            node_cost = self.__costtable[node][0]

            for neighbour in neighbours:

                neighbour_cost = self.__costtable[neighbour][0]

                if neighbour_cost > node_cost + self.graph[node][neighbour]:
                    self.__updatetable(self.__costtable, {neighbour:node_cost + self.graph[node][neighbour]})
                    self.__updatetable(self.__parenttable, {neighbour:node})

            self.__updatetable(self.__costtable, {node:True}, 1)

            node = self.__findlowest(self.__costtable)

        return self.__buildtracechain(self.__parenttable.copy(), self.end_point), self.__costtable[self.end_point][0]

    def getcosttable(self):

        return self.__costtable


if __name__=='__main__':

    graph_1 = {'A':{'B':5,
                    'C':2
                    },
               'B':{'D':4,
                    'E':2
                    },
               'C':{'E':7,
                    'B':8
                    },
               'D':{'F':3,
                    'E':6
                    },
               'E':{'F':1
                    },
               'F':{}
               }

    graph_2 = {'A': {'B': 10
                     },
               'B': {'C': 20
                     },
               'C': {'D': 1,
                     'E': 30
                     },
               'D': {'B': 1
                     },
               'E': {}
               }

    graph_3 = {'start': {'A': 6,
                         'B': 2
                         },
               'A': {'end': 1
                     },
               'B': {'A': 3,
                     'end': 5
                     },
               'end': {}
               }

    d = MyDijkstra(graph_3)

    print(d.findpath('start'))
