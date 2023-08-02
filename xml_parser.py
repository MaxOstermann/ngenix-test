import zipfile
from xml.etree import ElementTree
import multiprocessing
import csv


class XmlParser:
    def __init__(self, num_archives: int, num_files_per_archive: int) -> None:
        self.num_archives = num_archives
        self.num_files_per_archive = num_files_per_archive

    def parse_xml_files(self, archive_filename: str) -> list[dict[str, str]]:
        """ Парсинг XML-файлов в zip-архиве и возврат списка словарей """
        xml_data = []
        with zipfile.ZipFile(archive_filename, "r") as zip_file:
            for i in range(self.num_files_per_archive):
                xml_filename = f"file_{i}.xml"
                with zip_file.open(xml_filename) as xml_file:
                    xml_string = xml_file.read()
                    root = ElementTree.fromstring(xml_string)
                    xml_dict = {"id": root.find("var[@name='id']").get("value"),
                                "level": root.find("var[@name='level']").get("value")}
                    objects = root.find("objects")
                    for obj in objects.findall("object"):
                        xml_dict["object_name"] = obj.get("name")
                        xml_data.append(xml_dict.copy())
        return xml_data

    def process_archives(self) -> None:
        """ Обработка всех архивов и запись данных в CSV-файлы """
        pool = multiprocessing.Pool()
        archive_filenames = [f"archive_{i}.zip" for i in range(self.num_archives)]
        xml_data = pool.map(self.parse_xml_files, archive_filenames)
        pool.close()
        pool.join()

        # Запись данных в CSV-файлы
        with open("file1.csv", "w", newline="") as file1:
            writer = csv.writer(file1)
            writer.writerow(["id", "level"])
            for d in xml_data:
                for row in d:
                    writer.writerow([row["id"], row["level"]])

        with open("file2.csv", "w", newline="") as file2:
            writer = csv.writer(file2)
            writer.writerow(["id", "object_name"])
            for d in xml_data:
                for row in d:
                    writer.writerow([row["id"], row["object_name"]])
