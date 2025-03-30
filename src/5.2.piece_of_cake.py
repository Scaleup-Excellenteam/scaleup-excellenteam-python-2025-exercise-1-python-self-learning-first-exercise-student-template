
from typing import Dict,List

def piece_of_cake(dictionary:Dict[str,float] ,optional:List[str] = [],**kwargs) -> float:
    """
    Computes a weighted sum of values from the given dictionary, based on percentages provided
    in keyword arguments, while ignoring optional keys.
    """
    try:
        return sum(kwargs[name]/100 * dictionary[name] for name in kwargs if name not in optional )
    except KeyError:
        print("KeyError")
        return None

if __name__ == '__main__':
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, coco=200, milk=100))