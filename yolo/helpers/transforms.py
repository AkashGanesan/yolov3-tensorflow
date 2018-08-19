from itertools import zip_longest
from typing import Dict, Tuple, List, Any, NoReturn
from typing import Mapping, Sequence, Union, Mapping, Iterable
import ast

def sepToList(s : str, sep : str) ->list:
    return s.split(sep)


def tryCastNumeric(s : str) -> Union[int,float, str]:
    if type(s) is str:
        s = s.strip()
        if s.isnumeric():
            return int(s)
        elif "." in s:
            return float(s)
        else:
            return s
    
def strIsCommaSepList(s : str,
                      sep=",") -> bool:
    return sep in s


def tryStrToList(s: str,
                 sep = ","):    
    if strIsCommaSepList(s):
        return s.split(sep)
    return s


def applyCasts(s : Union[str,List,None]) -> Union[str,List[Union[str, int, float, None]]]:
    if s is None:
        return None
    s = tryStrToList(s)
    if (type(s) is str):
        return tryCastNumeric(s)
    elif type(s) is list:
        return list(map(applyCasts,s))
            
def unsafeTransformDict(d : Dict) -> NoReturn:
    mutate_dict(applyCasts, d)
    mutate_dict(lambda x: list(grouper(x,2)), d, filterOnVal=trueIfEqual)
            



# def tryCastNumeric(s : Union[str, List, None]) -> Union[str,int]:
#     if s is None:
#         return None
#     elif type(s) is str:
#         s = s.strip()
#         if s.isnumeric():
#             return int(s.strip())
#         elif "." in s:
#             try: 
#                 return float(s)
#             except:
#                 return s
#     elif type(s) is list:
#         return  list(map(tryCastNumeric,s))    
#     else:
#         return s

def trueAlways(v):
    return True

def trueIfEqual(v, eqVal="anchors"):
    return (v == eqVal)

def mutate_dict(f : Mapping[Any, Any]
                ,d : Dict
                ,filterOnVal=trueAlways):
    for k, v in d.items():
        if v is not None and filterOnVal(k):
            d[k] = f(v)


            
def grouper(iterable : Iterable,
            n : int,
            fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)        


        
if __name__=="__main__":
    print ("THis is sparta")
