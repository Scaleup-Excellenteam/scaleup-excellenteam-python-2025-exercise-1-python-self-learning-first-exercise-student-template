import os


def print_the_file_list(file_list, dir_path):
    """
    Print All The Files That Start With 'deep', Otherwise Print 'No Files That Start With Deep In The Directory'.
    """

    if (len(file_list) != 0):

        print(f'We Fount {len(file_list)} Files That Start With \'deep\' In {dir_path}')

        for i in range(0, len(file_list)):
            print(f'{i + 1}. {file_list[i]}')

    else:
        print(f'No Files That Start With \'deep\' In {dir_path}')


def thats_the_way(dir_path):
    """
    Return All The Files In The Parameter Directory That Start With 'deep'
    """
    files_list = []

    # Geting All The Files Names In The Directory, And Check Any One Of Them Start With 'deep'.
    for file in os.listdir(dir_path):
        if file.startswith('deep'):
            files_list.append(file)

    return files_list


def main():
    print_the_file_list(
        thats_the_way("C:\\Users\\97254\\Desktop\\Excellenteam\\Excellenteam Advanced Python\\Ex\\images"),
        "C:\\Users\\97254\\Desktop\\Excellenteam\\Excellenteam Advanced Python\\Ex\\images")


if __name__ == '__main__':
    main()
