import logging


def create_file(file_path, n=10):
    with open(file_path, 'w') as file:
        for i in range(0, n):
            file.writelines(f"This is line {i}\n")


def read_file(file_path):
    with open(file_path, 'r') as file:
        for l in file:
            logging.info(f"Red line: %s", l.removesuffix('\n'))


def read_file_max_chars(file_path, max_chars=99999999999999999):
    with open(file_path, 'r') as file:
        while True:
            next = file.readline(max_chars).removesuffix("\n")
            if len(next) == 0:
                break
            logging.info(f"Red line: {next}")


def copy_file(file_read, file_write):
    with open(file_read, 'r') as readfile:
        with open(file_write, 'w') as writefile:
            for line in readfile:
                writefile.write(line)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    create_file('testFile.txt')
    read_file('testFile.txt')
    read_file_max_chars('testFile.txt', 10)
    copy_file('testFile.txt','testFile.copy.txt')
