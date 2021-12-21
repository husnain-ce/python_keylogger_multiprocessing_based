import os,fnmatch,py7zr
from zipfile import ZipFile
from components.fileManipulation import FileManipulation

class ZipFiles:
    def __init__(self):
        self.file_path = os.getcwd() + "\\" + "secure.zip"
        file_manipulation = FileManipulation("cap_li",["*.enc"])
        self.file_to_zip = file_manipulation.cap_file_list()
        
    def make_zip(self):
        with ZipFile(self.file_path, 'w') as zipObj2:
            for file in self.file_to_zip:
                zipObj2.write(file)

    def make7_zip(self):
        with py7zr.SevenZipFile('CV.7z', 'w', password='jonathanjonathanwakeupwakeup') as archive:
            archive.writeall(self.file_path, self.file_path)

            