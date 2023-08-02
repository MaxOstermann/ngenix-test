import os
import random
import string
import zipfile
from xml.etree.ElementTree import Element, SubElement, tostring


class XmlGenerator:
    """  """
    def __init__(self, num_archives: int, num_files_per_archive: int, output_dir: str = '') -> None:
        self.num_archives = num_archives
        self.num_files_per_archive = num_files_per_archive
        self.output_dir = output_dir

    def generate_xml_data(self) -> bytes:
        """ Генерация случайных данных для XML-файла """
        root = Element("root")
        SubElement(root, "var", name="id", value=self.get_random_string())
        SubElement(root, "var", name="level", value=str(random.randint(1, 100)))
        objects = SubElement(root, "objects")
        for k in range(random.randint(1, 10)):
            SubElement(objects, "object", name=self.get_random_string())
        return tostring(root)

    @staticmethod
    def get_random_string(length: int = 10) -> str:
        """ Генерация случайной строки заданной длины """
        letters = string.ascii_lowercase
        return "".join(random.choice(letters) for _ in range(length))

    def generate_archives(self) -> None:
        """ Создание num_archives zip-архивов """
        for i in range(self.num_archives):
            zip_filename = os.path.join(self.output_dir, f"archive_{i}.zip")
            with zipfile.ZipFile(zip_filename, "w") as zip_file:
                # Создание num_files_per_archive XML-файлов в каждом архиве
                for j in range(self.num_files_per_archive):
                    xml_filename = f"file_{j}.xml"
                    xml_data = self.generate_xml_data()
                    zip_file.writestr(xml_filename, xml_data)
