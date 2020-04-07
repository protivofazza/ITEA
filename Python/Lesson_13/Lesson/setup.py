from typing import Tuple, List, Union, Dict, Any, Optional


# def is_magic(string_tuple: Tuple[Union[int, str], str, Union[int, float]]) -> bool:
#    for string in string_tuple:
#        if string.startswith('__'):
#            return True
#    return False

def is_magic(values_tuple):
    for value in values_tuple:
        print(value)

    return True


# print(is_magic((123, 'dsfsd', 123)))


def one_more_func(dict_obj: Dict[str, int],
                  any_type_arg: Any,
                  optional_arg: Optional[str] = None):
    print(dict_obj)


my_dict = {1: 2}

one_more_func(my_dict)
