""" Команда генерации архивов """
import click
from xml_generator import XmlGenerator


@click.command()
@click.option('--num_archives', default=50, help='Колчество архивов.')
@click.option('--num_files_per_archive', default=100, help='Колчество файлов в архиве.')
def xml_generator_command(num_archives, num_files_per_archive):
    """ запуск Generator """
    xml_generator = XmlGenerator(num_archives, num_files_per_archive)
    xml_generator.generate_archives()


if __name__ == '__main__':
    xml_generator_command()
