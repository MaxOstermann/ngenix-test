""" Тестирование генерации архивов """
import os
import pytest
from config import OUTPUT_DIR
from xml_generator import XmlGenerator


class TestXmlGenerator:
    """ тест генерация архивов """
    @pytest.fixture
    def xml_generator(self):
        return XmlGenerator(50, 100, output_dir=OUTPUT_DIR)

    def test_generate_xml_data(self, xml_generator):
        """Тестирование генерации XML-данных """
        xml_data = xml_generator.generate_xml_data()
        assert xml_data is not None

    def test_generate_zip_archive(self, xml_generator):
        """Тестирование генерации zip-архива """
        xml_generator.generate_archives()
        assert self.archive_exists()

    def test_get_random_string(self, xml_generator):
        """Тестирование генерации случайной строки """
        random_string = xml_generator.get_random_string(length=10)
        assert len(random_string) == 10

    def archive_exists(self) -> bool:
        """
        Проверка существования zip-архива.

        Returns:
            True, если архив существует, иначе False.
        """
        archive_path = os.path.join(OUTPUT_DIR, "archive_0.zip")
        return os.path.exists(archive_path) and os.path.isfile(archive_path)
