""" Тестирование генерации архивов """
import os
import pytest
from xml_parser import XmlParser


class TestXmlParser:
    @pytest.fixture
    def xml_parser(self):
        return XmlParser(1, 1)

    def test_parse_xml_file(self, xml_parser):
        """ Тестирование парсинга XML-файла"""
        xml_data = xml_parser.parse_xml_files("archive_0.zip")
        assert 1 <= len(xml_data) <= 10
        assert xml_data[0]["id"] is not None
        assert xml_data[0]["level"] is not None
        assert xml_data[0]["object_name"] is not None

    def test_write_to_csv(self, xml_parser):
        """ Тестирование записи данных в CSV-файл """
        xml_parser.process_archives()
        assert os.path.exists("file1.csv")
        assert os.path.exists("file2.csv")
