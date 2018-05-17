from django.db import models


# Create your models here.
class Betrieb(models.Model):
    name = models.CharField('Name', max_length=100)
    manager = models.CharField('Betriebsleiter', max_length=200)
    email = models.EmailField('Kontakt Email')
    arbeitnehmerzahl = models.IntegerField('Anzahl Arbeitnehmer',
                                           default=0,
                                           help_text='Gesamtzahl aller angestellten '
                                           'Arbeitnehmer/-innen inklusive Betriebsleiter/-innen')
    arbeitnehmerzahl.short_description = 'Stellen'
    raumforderung = models.FloatField('Raumanforderung', default=0,
                                      help_text='In Zahlen ausgedrückter '
                                      'Raumwunsch (halber Raum = 0,5)')
    raum = models.IntegerField('Raum', default=102)
    aufsicht = models.CharField('Aufsicht', max_length=100, default='keine')
    kredit = models.IntegerField('Kreditwunsch', default=0)
    business_idea = models.TextField('Idee')
    ip_address = models.CharField('IP Adresse', max_length=50, blank=True)
    confirmed = models.BooleanField('Bestätigt', default=False)
    approved = models.BooleanField('Zugelassen', default=False)

    def arbeitnehmerzahl_kurz(self):
        return self.arbeitnehmerzahl
    arbeitnehmerzahl_kurz.short_description = 'Stellen'

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Betrieb'
        verbose_name_plural = 'Betriebe'


class Partei(models.Model):
    name = models.CharField('Name', max_length=100)
    abbreviation = models.CharField('Abkürzung', max_length=5)
    chef = models.CharField('Parteivorsitzende', max_length=200)
    email = models.EmailField('Kontakt Email')
    description = models.TextField('Beschreibung (Ziele etc.)')
    ip_address = models.CharField('IP Adresse', max_length=50, blank=True)
    confirmed = models.BooleanField('Bestätigt', default=False)
    approved = models.BooleanField('Zugelassen', default=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Partei'
        verbose_name_plural = 'Parteien'


class PresidentCandidate(models.Model):
    name = models.CharField('Name', max_length=100)
    email = models.EmailField('Kontakt Email')
    motivation = models.TextField('Motivation')
    ip_address = models.CharField('IP Adresse', max_length=50, blank=True)
    confirmed = models.BooleanField('Bestätigt', default=False)
    approved = models.BooleanField('Zugelassen', default=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Präsidentschaftskandidat'
        verbose_name_plural = 'Präsidentschaftskandidaten'


class Question(models.Model):
    subject = models.CharField('Betreff', max_length=100)
    email = models.EmailField('Kontakt Email')
    content = models.TextField('Inhalt')
    ip_address = models.CharField('IP Adresse', max_length=50, blank=True)
    answered = models.BooleanField('Beantwortet', default=False)

    def __str__(self):
        return str(self.subject)

    class Meta:
        verbose_name = 'Frage'
        verbose_name_plural = 'Fragen'
