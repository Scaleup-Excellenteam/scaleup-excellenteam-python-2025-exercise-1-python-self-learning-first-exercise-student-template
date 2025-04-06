import time

def timer(f, a, b):
    """
    מודדת את הזמן שלוקחת לפונקציה f לרוץ עם הפרמטרים שניתנים לה.
        Param f - פונקציה
        Param a,b - פרמטרים
    """
    start_time = time.time()  # זמן התחלה
    f(a, b)  # קריאה לפונקציה f עם הפרמטרים
    end_time = time.time()  # זמן סיום
    print(f"Execution time: {end_time - start_time:.4f} seconds")  # הדפסת זמן הריצה

def example_function(x, y): # פונקצית דוגמה לניסוי
    time.sleep(1)  # לדוגמה, השהייה של 1 שנייה
    return x + y

def main():
    timer(example_function, 5, 3)

if(__name__=="__main__"):
    main()