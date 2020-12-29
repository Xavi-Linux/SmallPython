
class MyGrid:

    def __init__(self, header:str, column:str):

        self.header_text = header
        self.column_text = column
        self.header = [letter for letter in header]
        self.column = [letter for letter in column]
        self.__matrix = [[' ' for _ in range(0,len(self.header))] for _ in range(0,len(self.column))]

    def __getitem__(self, item):

        arg_type = type(item).__name__

        if arg_type == 'int' or arg_type == 'slice':

            return self.__matrix[item]

        elif arg_type == 'tuple':

            type_0, type_1 = type(item[0]).__name__, type(item[1]).__name__

            if type_0 == 'int':

                return self.__matrix[item[0]][item[1]]

            elif type_0 == 'slice':

                sub_matrix = []

                for row in self.__matrix[item[0]]:

                    sub_matrix += [row[item[1]]]

                return sub_matrix

        return None

    def __setitem__(self, key, value):

        key_type = type(key).__name__

        value_type = type(value).__name__

        value_eval = value_type == 'int' or value_type == 'float'

        if not value_eval:

            raise TypeError('value must be either integer or float!')

        if key_type == 'int':

            for i in range(0,len(self.__matrix[key])):

                self.__matrix[key][i] = value

        elif key_type == 'slice':

            start = 0 if key.start is None else key.start

            stop = len(self.__matrix) if key.stop is None else key.stop

            step = 1 if key.step is None else key.step

            for ind in range(start, stop, step):

                for j in range(0, len(self.__matrix[ind])):

                    self.__matrix[ind][j] = value

        elif key_type == 'tuple':

            type_0, type_1 = type(key[0]).__name__, type(key[1]).__name__

            if type_0 == 'int' and type_1 == 'int':

                self.__matrix[key[0]][key[1]] = value

            elif type_0 == 'int' and type_1 == 'slice':

                start = 0 if key[1].start is None else key[1].start

                stop = len(self.__matrix[key[0]]) if key[1].stop is None else key[1].stop

                step = 1 if key[1].step is None else key[1].step

                for col in range(start, stop, step):

                    self.__matrix[key[0]][col] = value

            elif type_0 == 'slice' and type_1 == 'int':

                start = 0 if key[0].start is None else key[0].start

                stop = len(self.__matrix) if key[0].stop is None else key[0].stop

                step = 1 if key[0].step is None else key[0].step

                for row in range(start, stop, step):

                    self.__matrix[row][key[1]] = value

            elif type_0 == 'slice' and type_1 == 'slice':

                start_row = 0 if key[0].start is None else key[0].start

                stop_row = len(self.__matrix) if key[0].stop is None else key[0].stop

                step_row = 1 if key[0].step is None else key[0].step

                start_col = 0 if key[1].start is None else key[1].start

                stop_col = len(self.__matrix[0]) if key[1].stop is None else key[1].stop

                step_col = 1 if key[1].step is None else key[1].step

                for row in range(start_row, stop_row, step_row):

                    for col in range(start_col, stop_col, step_col):

                        self.__matrix[row][col] = value

    def __str__(self):

        espaces_len = max(list(map(lambda a: max(list(map(lambda b: len(str(b)),a))), self.__matrix)))

        separator = ' | '

        matrix_repr = ' ' + separator

        for cell in self.header:

            remaining_spaces = espaces_len - len(str(cell))

            matrix_repr += ' '* remaining_spaces + str(str(cell)) + separator

        matrix_repr += '\n'

        for i, column in enumerate(self.column):

            matrix_repr += str(column) + separator

            for cell in self.__matrix[i]:

                remaining_spaces = espaces_len - len(str(cell))

                matrix_repr += ' '* remaining_spaces + str(cell) + separator

            matrix_repr += '\n'

        return matrix_repr


class MyDynamics:

    def __init__(self, text_1: str, text_2: str):

        self.text_1 = text_1 if len(text_1) >= len(text_2) else text_2
        self.text_2 = text_2 if len(text_2) <= len(text_1) else text_1
        self.lcstr_grid, self.lcseq_grid, self.levenshtein_grid = None, None, None

    def longest_common_substring(self):

        self.lcstr_grid = MyGrid(self.text_1, self.text_2)

        max_count = 0

        indexes = [0,0]

        top_left_exists = lambda a, b: a - 1 > -1 and b - 1 > -1

        for ih, letter_h in enumerate(self.lcstr_grid.header):

            for ir, letter_r in enumerate(self.lcstr_grid.column):

                if letter_h != letter_r:

                    self.lcstr_grid[ir, ih] = 0

                else:

                    if top_left_exists(ir, ih):

                        self.lcstr_grid[ir, ih] = 1 + self.lcstr_grid[ir - 1, ih - 1]

                    else:

                        self.lcstr_grid[ir, ih] = 1

                    if self.lcstr_grid[ir, ih] > max_count:

                        max_count = self.lcstr_grid[ir, ih]

                        indexes[0], indexes[1] = ir, ih

        common_substring = ''

        while max_count != 0 and top_left_exists(indexes[0] + 1, indexes[1] + 1):

            common_substring += self.lcstr_grid.header[indexes[1]]

            indexes[0] -= 1
            indexes[1] -= 1
            max_count = self.lcstr_grid[indexes[0],indexes[1]]

        return common_substring[::-1]

    def longest_common_subsequence(self):

        self.lcseq_grid = MyGrid(self.text_1, self.text_2)

        max_count = 0

        indexes = [0,0]

        top_left_exists = lambda a, b: a - 1 > -1 and b - 1 > -1

        for ir, letter_r in enumerate(self.lcseq_grid.column):

            for ih, letter_h in enumerate(self.lcseq_grid.header):

                if letter_h != letter_r:

                    self.lcseq_grid[ir, ih] = max_count

                else:

                    if top_left_exists(ir, ih):

                        self.lcseq_grid[ir, ih] = 1 + self.lcseq_grid[ir - 1, ih - 1]

                    else:

                        self.lcseq_grid[ir, ih] = 1

                    if self.lcseq_grid[ir, ih] >= max_count:

                        max_count = self.lcseq_grid[ir, ih]

                        indexes[0], indexes[1] = ir, ih

        common_subsequence = ''

        while max_count !=0:

            if self.lcseq_grid.header[indexes[1]] == self.lcseq_grid.column[indexes[0]]:

                common_subsequence += self.lcseq_grid.column[indexes[0]]

                indexes[0] -= 1 if indexes[0] > 0 else 0
                indexes[1] -= 1 if indexes[1] > 0 else 0
                max_count -= 1

            else:

                if self.lcseq_grid[indexes[0]-1,indexes[1]] >= self.lcseq_grid[indexes[0], indexes[1]]:

                    indexes[0] -= 1

                else:

                    indexes[1] -= 1

                if indexes[0] < 0:

                    indexes[1] += indexes[0]
                    indexes[0] = 0

                elif indexes[1] < 0:

                    indexes[0] += indexes[1]
                    indexes[1] = 0

        return common_subsequence[::-1]

    def levenshtein(self, sub_cost=1, ins_cost=0.5):

        if len(self.text_1) == 0:

            return len(self.text_2)

        elif len(self.text_2) == 0:

            return len(self.text_1)

        elif self.text_1 == self.text_2:

            return 0

        self.levenshtein_grid = MyGrid(' ' + self.text_1, ' ' + self.text_2)

        index_exists = lambda a, b: a - 1 > -1 and b - 1 > -1

        for ir in range(0, len(self.levenshtein_grid.column)):

            for ih in range(0,len(self.levenshtein_grid.header)):

                if ih == ir == 0:

                    self.levenshtein_grid[ir, ih] = 0

                    continue

                if self.levenshtein_grid.header[ih] == self.levenshtein_grid.column[ir]:

                    min_value = min(self.levenshtein_grid[ir-1, ih-1] if index_exists(ir,ih) else float('inf'),
                                    self.levenshtein_grid[ir-1, ih] + ins_cost if index_exists(ir,1) else float('inf'),
                                    self.levenshtein_grid[ir, ih-1] + ins_cost if index_exists(1,ih) else float('inf')
                                    )

                else:

                    min_value = min(self.levenshtein_grid[ir-1, ih-1] + sub_cost if index_exists(ir,ih) else float('inf'),
                                    self.levenshtein_grid[ir-1, ih] + ins_cost if index_exists(ir,1) else float('inf'),
                                    self.levenshtein_grid[ir, ih-1] + ins_cost if index_exists(1,ih) else float('inf')
                                    )

                self.levenshtein_grid[ir, ih] = min_value

        return self.levenshtein_grid[len(self.levenshtein_grid.column_text) - 1,
                                     len(self.levenshtein_grid.header_text) - 1]


if __name__ == '__main__':

    c = MyDynamics('fish', 'fishes')

    print(c.levenshtein())
    print(c.levenshtein_grid)








