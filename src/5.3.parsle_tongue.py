import re

def extract_secret_messages(file_path):
    """
    פותח את הקובץ לקריאה בינארית ומחפש מחרוזות סודיות
    המורכבות מאותיות אנגליות קטנות באורך 5 תווים לפחות ומסתיימות בסימן קריאה.
    """
    pattern = re.compile(rb'[a-z]{5,}!')
    messages = []
    
    with open(file_path, 'rb') as file:
        while chunk := file.read(1024):  # קריאה מדורגת של 1024 בתים בכל פעם
            messages.extend(match.group().decode() for match in pattern.finditer(chunk))
    return messages
def main():
# דוגמאות שימוש
    file_path = "resources/logo.jpg"
    secret_messages = extract_secret_messages(file_path)
    print(secret_messages)

if(__name__=="__main__"):
    main()