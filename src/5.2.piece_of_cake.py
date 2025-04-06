
def get_recipe_price(prices, optionals=None, **quantities):
    """
    מקבלת מילון של מחירי רכיבים ל-100 גרם, רשימה של רכיבים אופציונליים להתעלמות, 
    וכמות נדרשת מכל רכיב, ומחזירה את המחיר הכולל של המצרכים.
    """
    optionals = optionals or []
    return int(sum((prices[item] * quantities[item]) / 100 for item in quantities if item in prices and item not in optionals))
def main():
# דוגמאות שימוש
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))  # מחזיר 44
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))  # מחזיר 54
    print(get_recipe_price({}))  # מחזיר 0
    
if(__name__=="__main__"):
    main()