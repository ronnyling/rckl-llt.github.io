""" Python file related to common component - file upload """
import fnmatch
import os
from pathlib import Path

from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn


class FileUpload(PageObject):
    """ Functions related to file upload """
    FILE_PATH = "${file_path}"
    _locators = {
        "file_type": "//input[@type='file']"
    }

    def search_random_file(self, file_type):
        """ Functions to create file path based on random file """
        base_path = Path(__file__).parent.parent
        file_type = file_type.lower()
        if file_type in ["png", "jpeg", "jpg"]:
            file = 'Images'
        elif file_type in ["pdf", "docx", "xlsx", "pptx", "zip"]:
            file = 'files'
        elif file_type in ["pdf", "mp4", "mov", "avi"]:
            file = 'movies'
        random_file = f'*.{file_type}'
        filepath = (base_path / "../setup/testdata" / file).resolve()
        print(filepath)
        file_dir = os.listdir(filepath)
        for file_search in file_dir:
            if fnmatch.fnmatch(file_search, random_file):
                file_path = Path(filepath / file_search)
                BuiltIn().set_test_variable(self.FILE_PATH, file_path)

    def search_specific_file(self, file_name):
        """ Functions to create file path based on specific file """
        base_path = Path(__file__).parent.parent
        selected_file = f'{file_name}'
        file = 'PlaybookContent'
        filepath = (base_path / "../setup/testdata" / file).resolve()
        print(filepath)
        file_dir = os.listdir(filepath)
        for file_search in file_dir:
            if fnmatch.fnmatch(file_search, selected_file):
                file_path = Path(filepath / file_search)
                BuiltIn().set_test_variable(self.FILE_PATH, file_path)

    def choose_the_file_to_upload(self):
        """ Functions to select file to upload based on file path """
        file_path = BuiltIn().get_variable_value(self.FILE_PATH)
        print("file_path", file_path)
        file_name = self.get_uploaded_file_name(file_path)
        print("file_name", file_name)
        file_size = self.get_uploaded_file_size(file_path)
        print("file_size", file_size)
        print("str file path", str(file_path))
        self.selib.choose_file(self.locator.file_type, str(file_path))
        self._wait_for_page_refresh()

    def get_uploaded_file_name(self, file_path):
        """ Functions to retrieve uploaded file name """
        base = os.path.basename(file_path)
        return base

    def get_uploaded_file_size(self, file_path):
        """ Functions to retrieve uploaded file size """
        size = os.path.getsize(file_path)
        size = size / 1000
        size = round(size, 2)
        size = str(size)
        return size
