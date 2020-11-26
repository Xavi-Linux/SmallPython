"""
Write a Python class to convert an integer to a roman numeral.
"""
import sys

class roman:
    __conv = {'I': {'v': 1, 'm': 3},
              'V': {'v': 5, 'm': 8},
              'X': {'v': 10, 'm': 39},
              'L': {'v': 50, 'm': 89},
              'C': {'v': 100, 'm': 399},
              'D': {'v': 500, 'm': 899},
              'M': {'v': 1000, 'm': 3999}}

    def __init__(self, val: int):
        if type(val).__name__ == 'int':
            self.__val = val

        else:
            raise TypeError('it must be an integer')

    def convert(self) -> str:
        vals = []
        for i in range(0, len(str(self.__val))):
            vals.append(str(self.__val)[i] + '0' * (len(str(self.__val))-1-i))

        cadena = ''
        for v in vals:
            cadena += self.__partialconv(int(v))
        return cadena

    def __partialconv (self, valor: int) -> str:
        if valor == 0:
            return ''
        res = ''
        for k, v in self.__conv.items():
            if v['m']/valor >= 1:
                if v['v'] <= valor:
                    res = str(k) + self.__partialconv(valor - v['v'])
                    return res
                else:
                    res = self.__partialconv(v['v'] - valor) + str(k)
                    return res


print(roman(int(sys.argv[1])).convert())

