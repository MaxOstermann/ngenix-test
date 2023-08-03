""" Команда parse """
import click
from xml_parser import XmlParser


@click.command()
@click.option('--num_archives', default=50, help='Колчество архивов.')
@click.option('--num_files_per_archive', default=100, help='Колчество файлов в архиве.')
def xml_parse_command(num_archives, num_files_per_archive):
    """ Запуск Parser"""
    xml_parser = XmlParser(num_archives, num_files_per_archive)
    xml_parser.process_archives()


if __name__ == '__main__':
    xml_parse_command()
