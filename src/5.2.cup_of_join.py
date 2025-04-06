#

def join(*lists, sep='-'):
    """
    מקבלת מספר בלתי מוגבל של רשימות ומחברת אותן לרשימה אחת עם מפריד בין הרשימות.
    """
    if not lists:
        return None
    
    result = []
    for i, lst in enumerate(lists):
        if i > 0:
            result.append(sep)
        result.extend(lst)
    
    return result

def main():
# דוגמאות שימוש
    print(join([1, 2], [8], [9, 5, 6], sep='@'))  
    print(join([1, 2], [8], [9, 5, 6])) 
    print(join([1]))
    print(join()) 

if(__name__=="__main__"):
    main()