import os


def check_file():
    if os.path.isfile(r"D:\temp\file.txt"):
        print("TestCase Passed")
    else:
        print("TestCase Failed")


if __name__ == "__main__":
    check_file()
