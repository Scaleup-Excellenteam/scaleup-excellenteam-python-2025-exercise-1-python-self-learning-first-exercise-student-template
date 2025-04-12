import re
import os


def parsle_tongue(file_path = None, data_part_size=1024):
    """
    Open The Logo In Binary Mode, Read It In Chunks, 
    And Extract Secret Messages Containing At Least 5 Lowercase English Letters Ending With An Exclamation Mark.
    """
    
    # If The User Don't Give A Path For The File.
    if file_path is None:
        file_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'logo.jpg')

    # Opening The File In Binary Mode.
    with open(file_path, 'rb') as file:
        
        secret_words = []
        
        # Reading Line From The File.
        data_part = file.read(data_part_size)

        # Reading The File Line By Line.
        while data_part:

            # Convert The Binary Charter To String, And Find All The Secret String.
            string_from_binary = data_part.decode(errors='ignore')
            secret_str = re.findall(r'[a-z]{5,}!', string_from_binary)

            for secret in secret_str:
                secret_word = secret.replace("!","")
                secret_words.append(secret_word)
                

            # Reading Anthoer Line From The File.
            data_part = file.read(data_part_size)

        file.close()
        
    return secret_words


def main():
    parsle_tongue("C:\\Users\\97254\\Desktop\\Excellenteam\\Excellenteam Advanced Python\\Ex\\resources\\logo.jpg")


if __name__ == "__main__":
    main()
