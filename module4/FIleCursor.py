import logging


def create_file(file, n=10):
    for i in range(0, n):
        file.writelines(f"This is line {i}\n")
    logging.info(f"Currently cursor is at {file.tell()}")


def read_file(file):
    for l in file:
        logging.info(f"Red line: %s", l.removesuffix('\n'))


def read_file_max_chars(file, max_chars=99999999999999999):
    while True:
        next = file.readline(max_chars).removesuffix("\n")
        # empty strings return false in python
        if not next:
            break
        logging.info(f"Red line: {next}")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    with open('testFile.txt', 'w+') as file:
        create_file(file)
        logging.info("Rading from offset 0")

        file.seek(0, 0)
        read_file(file)

        logging.info("Rading from offset 100")
        file.seek(100, 0)
        read_file(file)

        logging.info("Rading from offset 1000")
        file.seek(1000, 0)
        read_file(file)

        logging.info("Rading from offset 0 with max 10 characters")
        file.seek(0, 0)
        read_file_max_chars(file, 10)
