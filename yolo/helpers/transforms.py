from itertools import zip_longest
from typing import Dict, Tuple, List, Any, NoReturn
from typing import Mapping, Sequence, Union, Mapping, Iterable
import ast
from copy import deepcopy

def tryCastNumeric(s : str) -> Union[int,float, str]:
    """ 
    Given a string, it converts it to an int or float if possible;
    else returns the string as is"""
    if type(s) is str:
        s = s.strip()
        if s.isnumeric():
            return int(s)
        elif "." in s:
            return float(s)
        else:
            return s


        
def strIsCommaSepList(s : str,  sep=",") -> bool:
    """ Check if it the given string looks like a comma separated
    list"""
    return sep in s



def tryStrToList(s: str,
                 sep = ",") -> Union[str,List]:
    """ If comma separated list-like string, return a list, else
    return string as is"""
    if strIsCommaSepList(s):
        return s.split(sep)
    return s


def trueAlways(v : Any) -> bool:
    return True

def trueIfEqual(v : Any, eqVal="anchors") -> bool:
    """ Returns if v matches eqVal.  """
    return (v == eqVal)


def mutate_dict(f : Mapping[Any, Any]
                ,d : Dict
                ,filterOnKey=trueAlways) -> NoReturn:
    """ Aplly function over all values for keys satisfying filterOnKey """
    for k, v in d.items():
        if v is not None and filterOnKey(k):
            d[k] = f(v)


            
def grouper(iterable : Iterable,
            n : int,
            fillvalue=None) -> Iterable:
    """ Groups items in iterable with optional fill with a given value"""
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)        



class DarkNetTransformer:
    """ DarkNet transformer for cleaning up the list of dictionaries to a saner formate"""
    @classmethod
    def applyCasts(cls, s : Union[str,List,None]) -> Union[str,List[Union[str, int, float, None]]]:
        """ Applies numeric casts and comma sep list like strings to lists"""
        if s is None:
            return None
        s = tryStrToList(s)
        if (type(s) is str):
            return tryCastNumeric(s)
        elif type(s) is list:
            return list(map(cls.applyCasts,s))

    @classmethod        
    def transformDict(cls, d : Dict, inplace=True) -> NoReturn:
        """ Runs the darknet transformation over the dictionary"""
        if (inplace == False):
            d = deepcopy(d)
        cls._unsafeTransformDict(d)
        return d
    
    @classmethod        
    def _unsafeTransformDict(cls, d : Dict) -> NoReturn:
        mutate_dict(cls.applyCasts, d)
        mutate_dict(lambda x: list(grouper(x,2)), d, filterOnKey=trueIfEqual)


    @classmethod
    def transform(cls, lst : List, inplace=True) -> List[Dict]:
        if (inplace == False):
            d = deepcopy(d)
        cls._unsafeTransformDictLists(lst)
            
    @classmethod                
    def _unsafeTransformDictLists(cls, lst : List) -> NoReturn:
        list(map(cls.transformDict, lst))


        
if __name__=="__main__":
    pass
