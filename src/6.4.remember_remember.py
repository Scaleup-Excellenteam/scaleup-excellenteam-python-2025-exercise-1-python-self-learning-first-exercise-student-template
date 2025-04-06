from PIL import Image


def decrypt_message(image_path):
    """
    מקבלת נתיב לתמונה, ומחזירה את המסר המוצפן על ידי הפיקסלים השחורים.
    """
    image = Image.open(image_path)
    width, height = image.size  # מקבלים את ממדי התמונה
    message = ''

    # עבור כל עמודה בתמונה, בודקים היכן הפיקסל השחור נמצא ומפענחים את המסר
    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            # הדפסת ערך הפיקסל לצורך בדיקה
            print(f"Pixel at ({x}, {y}): {pixel}")

            if pixel == (0, 0, 0):  # אם הפיקסל צבוע בשחור
                print(f"Black pixel found at ({x}, {y}) -> Char: {chr(y)}")  # הדפסת המסר שנמצא
                message += chr(y)  # המיקום בשורה (y) הוא הערך של התו
                break

    return message
def main():
    # דוגמת שימוש
    image_path = '../resources/code.png'
    message = decrypt_message(image_path)
    print(f"Decrypted message: {message}")

if(__name__=="__main__"):
    main()