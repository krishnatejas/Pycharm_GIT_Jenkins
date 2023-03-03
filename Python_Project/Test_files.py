import os
import time


def check_file():
    if os.path.isfile(r"D:\temp\file.txt"):
        print("TestCase Passed")
    else:
        print("TestCase Failed")


if __name__ == "__main__":
    time.sleep(5)
    check_file()
