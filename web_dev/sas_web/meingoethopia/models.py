from django.db import models


# Create your models here.
class Betrieb(models.Model):
    name = models.CharField('Name', max_length=100)
    manager = models.CharField('Betriebsleiter', max_length=200)
    email = models.EmailField('Kontakt Email')
    business_idea = models.TextField('Idee')
    confirmed = models.BooleanField('Bestätigt', default=False)

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
    confirmed = models.BooleanField('Bestätigt', default=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Partei'
        verbose_name_plural = 'Parteien'


class PresidentCandidate(models.Model):
    name = models.CharField('Name', max_length=100)
    email = models.EmailField('Kontakt Email')
    motivation = models.TextField('Motivation')
    confirmed = models.BooleanField('Bestätigt', default=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Präsidentschaftskandidat'
        verbose_name_plural = 'Präsidentschaftskandidaten'
