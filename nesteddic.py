from typing import Union
from typing import Any


def nesteddic(dic: dict, k: Any) -> Any:
    def nestedlist(llista: Union[list, tuple]) -> Union[dict, None]:
        for el in llista:
            if type(el).__name__ == 'list' or type(el).__name__ == 'tuple':
                if nestedlist(el) is not None:
                    return nestedlist(el)
            elif type(el).__name__ == 'dict':
                if nesteddic(el, k) is not None:
                    return el
        return None
    for el in dic:
        if el == k:
            return dic[el]
        elif type(dic[el]).__name__ == 'dict':
            if nesteddic(dic[el], k) is not None:
                return nesteddic(dic[el], k)
        elif type(dic[el]).__name__ == 'list' or type(dic[el]).__name__ == 'tuple':
            if nestedlist(dic[el]) is not None:
                return nesteddic(nestedlist(dic[el]), k)
    return None


