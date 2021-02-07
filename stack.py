class MyStack:

    def __init__(self, vals=None):

        self.__stack = []

        if vals:

            self.append(vals)

    def pop_read(self):

        val = self.__stack.pop()

        return val

    def append(self,values):

        self.__stack.append(values)

    def is_empty(self):

        return len(self.__stack) == 0


def bracket_checker(text: str):
    """
    check if every opening bracket has its own closing counterpart (brackets, square brackets and curly brackets)
    """

    def point_error(err_str,pos):

        end = min(len(err_str)-pos, 6)

        return '\n' + err_str[pos:pos+end] + '\n^' + ' ' * (end - 1)

    stack = MyStack()

    targets = {'[':']',
               '(': ')',
               '{': '}'
               }

    is_opening = lambda l: l in targets.keys()

    is_closing = lambda l: l in targets.values()

    for i, letter in enumerate(text):

        if is_opening(letter):

            stack.append((letter, i))

        elif is_closing(letter):

            if stack.is_empty():

                raise SyntaxError('missing opening bracket for {0} at position {1}{2}'.format(letter, i, point_error(text, i)))

            opening = stack.pop_read()

            if letter != targets[opening[0]]:

                raise SyntaxError('mismatched opening bracket for {0} at position {1}{2}'.format(letter, opening[1], point_error(text, opening[1])))

    if not stack.is_empty():

        remainder = stack.pop_read()

        raise SyntaxError('missing closing bracket for {0} at position {1}{2}'.format(remainder[0],remainder[1], point_error(text, remainder[1])))


if __name__ == '__main__':

    cadena = '(){}{}{}}{}[][]'

    bracket_checker(cadena)


