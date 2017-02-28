import os
import shutil


class FileHandler:

    def delete(self, location):
        shutil.rmtree(location)

    def delete_file(self, location):
        os.remove(location)

    def create_directory(self, location):
        return os.makedirs(location)

    def archive(self, fileName, source, destination, format="zip"):
        destination = os.path.join(destination, fileName)
        shutil.make_archive(destination, format, source)


if __name__ == "__main__":
    fileHandler = FileHandler()
    fileHandler.archive("vai", "C:\\Users\\touhid\Desktop\\table\\test\\Materia\\HTML", "C:\\Users\\touhid\Desktop")