
import os
"""זו הדרך"""
def thats_the_way(directory: str):
    """
    מחזירה רשימה של כל הקבצים בתיקייה הנתונה שמתחילים ב-"deep"
    """
    try:
        return [file for file in os.listdir(directory) if file.startswith("deep")]
    except FileNotFoundError:
        print(f"Error: The directory '{directory}' was not found.")
        return []
    except PermissionError:
        print(f"Error: Permission denied for directory '{directory}'.")
        return []

def main():
# בדיקה על התיקייה 'images'
    result = list_deep_files("images")
    print(result)

# בדיקה אם נמצאו שני קבצים
    if len(result) == 2:
        print("Success: Found two files starting with 'deep'")
    else:
        print(f"Found {len(result)} files instead of 2.")

if(__name__=="__main__"):
    main()
