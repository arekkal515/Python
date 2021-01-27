# generate a file with random numbers

import random

def main():
    file_object = open("file.txt", "w+")
    for i in range(15000):
        file_object.write("{} {}\n".format(i+1, random.randint(1, 100)))
        # \r\n - new line in Windows
    file_object.close()

if __name__ == "__main__":
    main()