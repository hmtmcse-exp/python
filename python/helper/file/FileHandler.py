import json
import zipfile

from datetime import date, datetime

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

    def extract_zip(self, zip_file, extract_location):
        fh = open(zip_file, 'rb')
        z = zipfile.ZipFile(fh)
        for name in z.namelist():
            z.extract(name, extract_location)
        fh.close()

    def write_to_file(self, location):
        dictionary = dict()
        dictionary["last_log"] = "last_log_mia"
        dictionary["branch"] = "branch"
        dictionary["last_commit"] = "last_commit"
        json_string = json.dumps(dictionary)
        open_file = open(location, "w")
        open_file.write(json_string)

    def get_dir_list(self, path):
        return os.listdir(path)

if __name__ == "__main__":

    read_file = open("build_log", "r")
    data = read_file.read()
    d = json.loads(data)
    print(d["last_log"])

    print(str(datetime.now()))

    fileHandler = FileHandler()
    # fileHandler.write_to_file("C:\\Users\\touhid\\Desktop\\table\\test\\Materia\\ANGULAR\dist\\fonts\\ionicons\\css\\*")
    print(fileHandler.get_dir_list("C:\\Users\\touhid\\Desktop\\"))

    # fileHandler.archive("vai", "C:\\Users\\touhid\Desktop\\table\\test\\Materia\\HTML", "C:\\Users\\touhid\Desktop")
    # fileHandler.extract_zip("C:\\Users\\touhid\Desktop\\pythontest.zip", "C:\\Users\\touhid\Desktop\\table\\test\\Materia\\HTML\\X")