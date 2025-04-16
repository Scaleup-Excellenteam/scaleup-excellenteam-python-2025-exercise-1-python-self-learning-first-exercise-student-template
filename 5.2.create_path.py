def create_path(drive_letter, *parts):
    if not drive_letter:
        raise ValueError("Drive letter is required")
    path = drive_letter + ":"
    if parts:
        path += "\\" + "\\".join(parts)
    return path

if __name__ == '__main__':
    print(create_path("C", "Users", "Yam"))
    print(create_path("C", "Users", "Yam", "HaimonLimon.mp4"))
    print(create_path("D", "1337.png"))
    print(create_path("C"))
