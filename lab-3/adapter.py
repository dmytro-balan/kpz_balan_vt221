import sys

class Logger:
    def log(self, msg):
        print(f"\033[92m{msg}\033[0m")

    def error(self, msg):
        print(f"\033[91m{msg}\033[0m")

    def warn(self, msg):
        print(f"\033[93m{msg}\033[0m")

class FileWriter:
    def write(self, msg):
        with open("log.txt", "a") as file:
            file.write(msg)

    def writeln(self, msg):
        with open("log.txt", "a") as file:
            file.write(msg + "\n")

class FileLoggerAdapter(Logger):
    def __init__(self):
        self.file_writer = FileWriter()

    def log(self, msg):
        self.file_writer.writeln(f"[LOG] {msg}")

    def error(self, msg):
        self.file_writer.writeln(f"[ERROR] {msg}")

    def warn(self, msg):
        self.file_writer.writeln(f"[WARNING] {msg}")

def main():
    logger = Logger()
    logger.log("This is a log message")
    logger.error("This is an error message")
    logger.warn("This is a warning message")

    file_logger = FileLoggerAdapter()
    file_logger.log("This is a log message")
    file_logger.error("This is an error message")
    file_logger.warn("This is a warning message")

if __name__ == "__main__":
    main()