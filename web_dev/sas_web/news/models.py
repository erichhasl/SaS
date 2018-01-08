from django.db import models


# Create your models here.
class ParteiWerbung(models.Model):
    partei = models.ForeignKey('meingoethopia.Partei')

    def __str__(self):
        return str(self.partei)

    class Meta:
        verbose_name = 'Parteiwerbung'
        verbose_name_plural = 'Parteienwerbung'


class PraesidentWerbung(models.Model):
    partei = models.ForeignKey('meingoethopia.PresidentCandidate')

    def __str__(self):
        return str(self.partei)

    class Meta:
        verbose_name = 'Präsidentwerbung'
        verbose_name_plural = 'Präsidentenwerbung'
