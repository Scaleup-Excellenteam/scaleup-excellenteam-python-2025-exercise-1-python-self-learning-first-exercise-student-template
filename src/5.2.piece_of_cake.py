"""
This module defines a function `piece_of_cake` that computes a weighted sum of values from 
the given dictionary, based on percentages provided in keyword arguments. It ignores optional keys.

Function:
    piece_of_cake(prices, optionals=None, **kwargs):
        - Computes a weighted sum from the `prices` dictionary, excluding the optional keys.
        - Each item in `kwargs` represents a key-value pair where the key is a dictionary key and 
          the value is the percentage to multiply by the corresponding value in `prices`.
        - Returns the weighted sum as a float.
        - If a `KeyError` occurs, prints an error message and returns `None`.
"""
from typing import Dict, List

def piece_of_cake(prices: Dict[str, float] = None, optionals: List[str] = None, **kwargs) -> float:
    """
    Computes a weighted sum of values from the `prices` dictionary based on percentages provided 
    in the keyword arguments, excluding optional keys.
    Args:
        prices (Dict[str, float]): A dictionary where the keys are item names and the values are their prices.
        optionals (List[str]): A list of keys to ignore when calculating the weighted sum.
        **kwargs: A dictionary of key-value pairs where the keys are items in `prices` and 
                  the values are the corresponding percentages.
    Returns:
        float: The computed weighted sum or `None` if a `KeyError` occurs.
    """
    # Initialize default values for the parameters if they are None
    if prices is None:
        prices = {}
    if optionals is None:
        optionals = []

    try:
        # Compute the weighted sum, excluding optional keys
        return float(sum((kwargs[name] / 100) * prices[name] for name in kwargs if name not in optionals))
    except KeyError:
        print("KeyError: One of the provided keys does not exist in the prices dictionary.")
        return None


if __name__ == '__main__':
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, optionals=['milk'], coco=200, milk=100))
