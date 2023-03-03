import time


def file_creation():
    with open(r"D:\temp\file.txt", 'w') as f:
        f.write("Welcome Note")
        print("file created")


if __name__ == '__main__':
    file_creation()
    time.sleep(5)
    print("file creation done__")
