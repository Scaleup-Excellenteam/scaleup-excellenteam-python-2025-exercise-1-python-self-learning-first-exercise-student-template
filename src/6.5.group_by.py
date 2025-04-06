def group_by(func, iterable):
    """
    מקבלת פונקציה כפרמטר ראשון ו־iterable כפרמטר שני.
    מחזירה מילון שבו המפתחות הם הערכים שהפונקציה מחזירה עבור כל איבר, והערכים הם רשימות
    של כל האיברים שעבורם חזר אותו הערך.
    """
    result = {}
    for item in iterable:
        key = func(item)
        if key not in result:
            result[key] = []
        result[key].append(item)
    return result

def main():
# דוגמת שימוש
    print(group_by(len, ["hi", "bye", "yo", "try"]))

if(__name__=="__main__"):
    main()