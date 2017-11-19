from django.db import models


# Create your models here.
class Banned(models.Model):
    ip_address = models.CharField('IP Adresse', max_length=50)
    reason = models.TextField('Grund')

    class Meta:
        verbose_name = 'Verbannte'
        verbose_name_plural = 'Verbannte'
