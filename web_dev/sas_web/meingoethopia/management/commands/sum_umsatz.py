from django.core.management.base import BaseCommand
from meingoethopia.models import Betrieb


class Command(BaseCommand):
    args = 'filename'
    help = 'populate the angestellten database from an excel list'

    def gesamtumsatz(self):
        betriebe = Betrieb.objects.all()
        klassen = {}
        for b in betriebe:
            u = sum([a.umsatz for a in b.betriebsabrechnung_set.all()])
            u2 = u / b.angestellte.count()
            for a in b.angestellte.all():
                if a.klasse not in klassen:
                    klassen[a.klasse] = u2
                else:
                    klassen[a.klasse] += u2
        print(klassen)

    def handle(self, *args, **options):
        # filename = options['filename']
        self.gesamtumsatz()

    # def add_arguments(self, parser):
        # parser.add_argument('filename')
