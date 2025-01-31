import logging


def read_from_file_no_io_error(path):
    file = None
    try:
        file = open(path, "r")
        logging.info("Read from file: %s", file.read())
    except:
        logging.error("unknown error reading from file %s.", path, exc_info=True, stack_info=True)
    finally:
        if file is not None:
            file.close()
            logging.info("File closed")


def read_from_file_no_file_not_found_error(path):
    file = None
    try:
        file = open(path, "r")
        logging.info("Read from file: %s", file.read())
    except IOError:
        logging.error("io error reading from file %s.", path, exc_info=True, stack_info=True)
    except:
        logging.error("unknown error reading from file %s. %s", path, exc_info=True, stack_info=True)
    finally:
        if file is not None:
            file.close()
            logging.info("File closed")


def read_from_file(path):
    file = None
    try:
        with open(path, 'r') as file:
            logging.info("Read from file: %s", file.read())
    except FileNotFoundError:
        logging.error("could not find file %s", path, exc_info=True, stack_info=True)
    except IOError:
        logging.error("io error reading from file %s.", path, exc_info=True, stack_info=True)
    except:
        logging.error("unknown error reading from file %s.", path, exc_info=True, stack_info=True)
    else:
        logging.info("no error in reading file :)")
    finally:
        logging.info("in finally")


def write_to_file(path):
    file = None
    try:
        file = open(path, "w")
        file.write("Hello File :)")
        logging.info("Writen to file: %s", path)
    except IOError:
        logging.error("cannot write to file %s", path, exc_info=True, stack_info=True)
    except:
        logging.error("unknown error writing to file %s.", path, exc_info=True, stack_info=True)
    finally:
        if file is not None:
            file.close()
            logging.info("File closed")


def test():
    read_from_file('../PythonWorld.iml')
    read_from_file('./PythonWorld.iml')
    read_from_file_no_file_not_found_error("./PythonWorld.iml")
    read_from_file_no_io_error("./PythonWorld.iml")
    write_to_file("fileToWrite.txt")
    read_from_file_no_file_not_found_error("fileToWrite.txt")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    test()
