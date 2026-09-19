from abc import ABC, abstractmethod

class FileHandler(ABC):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass


class TextFileHandler(FileHandler):

    def read(self):
        print("Reading text file")

    def write(self, data):
        print("Writing:", data)


class BinaryFileHandler(FileHandler):

    def read(self):
        print("Reading binary file")

    def write(self, data):
        print("Writing binary data:", data)


text = TextFileHandler()
text.read()
text.write("Hello")

binary = BinaryFileHandler()
binary.read()
binary.write("101010")
