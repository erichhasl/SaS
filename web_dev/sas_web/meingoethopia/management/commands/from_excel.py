from django.core.management.base import BaseCommand
from meingoethopia.models import Angestellter
import xlrd


class Command(BaseCommand):
    args = 'filename'
    help = 'populate the angestellten database from an excel list'

    def populate_db(self, filename):
        book = xlrd.open_workbook(filename)
        sheet = book.sheets()[0]
        for row in [sheet.row_values(i) for i in range(sheet.nrows) if
                    sheet.row_values(i)[0]]:
            name, klasse = row
            vorname = name.split(', ')[1]
            nachname = name.split(', ')[0]
            name_final = vorname + " " + nachname
            print(name_final, klasse)
            Angestellter(name=name_final.replace('ć', 'c'), klasse=klasse,
                         is_teacher=False).save()

    def handle(self, *args, **options):
        filename = options['filename']
        self.populate_db(filename)

    def add_arguments(self, parser):
        parser.add_argument('filename')
