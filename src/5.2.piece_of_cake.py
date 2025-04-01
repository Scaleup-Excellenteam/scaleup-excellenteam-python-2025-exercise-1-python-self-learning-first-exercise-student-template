
from typing import Dict,List

def piece_of_cake(prices:Dict[str,float] ={}  ,optionals:List[str] = [],**kwargs) -> float:
    """
    Computes a weighted sum of values from the given dictionary, based on percentages provided
    in keyword arguments, while ignoring optional keys.
    """
    try:
        return float(sum(kwargs[name]/100 * prices[name] for name in kwargs if name not in optionals ))
    except KeyError:
        print("KeyError")
        return None

# def piece_of_cake(prices: Dict[str, float] = {}, optionals: List[str] = [], **kwargs) -> float:
#     """
#     Computes a weighted sum of values from the given dictionary, based on percentages provided
#     in keyword arguments, while ignoring optional keys.
#     """
#     total_weight = 0.0
#     for name, percentage in kwargs.items():
#         if name not in optionals and name in prices:
#             total_weight += (percentage / 100) * prices[name]
#     return total_weight

if __name__ == '__main__':
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, coco=200, milk=100))
