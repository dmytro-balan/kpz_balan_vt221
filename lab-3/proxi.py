import re
class SmartTextReader:
    def __init__(self, filename):
        self.filename = filename
    def read(self):
        with open(self.filename, 'r') as file:
            lines = file.readlines()
        return [list(line.strip()) for line in lines]
    def get_filename(self):
        return self.filename
class SmartTextChecker:
    def __init__(self, smart_text_reader):
        self.smart_text_reader = smart_text_reader
    def read(self):
        try:
            print(f"Opening file: {self.smart_text_reader.get_filename()}")
            content = self.smart_text_reader.read()
            print(f"Successfully read the file: {self.smart_text_reader.get_filename()}")
            num_lines = len(content)
            num_chars = sum(len(line) for line in content)
            print(f"Total lines: {num_lines}")
            print(f"Total characters: {num_chars}")
            return content
        except Exception as e:
            print(f"Error reading file: {e}")
            return None
        finally:
            print(f"Closing file: {self.smart_text_reader.get_filename()}")
    def get_filename(self):
        return self.smart_text_reader.get_filename()
class SmartTextReaderLocker:
    def __init__(self, smart_text_reader, pattern):
        self.smart_text_reader = smart_text_reader
        self.pattern = re.compile(pattern)
    def read(self):
        if self.pattern.match(self.smart_text_reader.get_filename()):
            print("Access denied!")
            return None
        else:
            return self.smart_text_reader.read()
def main():
    filename = "example.txt"
    reader = SmartTextReader(filename)
    checker = SmartTextChecker(reader)
    locker = SmartTextReaderLocker(checker, r'.*\.lock$')
    content = locker.read()
    if content:
        for line in content:
            print("".join(line))
if __name__ == "__main__":
    main()
