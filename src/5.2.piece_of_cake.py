
from typing import Dict,List

def piece_of_cake(prices:Dict[str,float] ={}  ,optionals:List[str] = None,**kwargs) -> float:
    """
    Computes a weighted sum of values from the given dictionary, based on percentages provided
    in keyword arguments, while ignoring optional keys.
    """
    try:
        return float(sum(kwargs[name]/100 * prices[name] for name in kwargs if name not in optionals ))
    except KeyError:
        print("KeyError")
        return None


if __name__ == '__main__':
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, coco=200, milk=100))
