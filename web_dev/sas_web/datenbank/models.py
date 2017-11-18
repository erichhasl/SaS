from django.db import models


# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titel')
    pub_date = models.DateTimeField('Veröffentlichungsdatum')
    image = models.ImageField('Vorschaubild', upload_to='thumbnails')
    element = models.FileField('Datei', upload_to='datastorage')

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Eintrag'
        verbose_name_plural = 'Einträge'
