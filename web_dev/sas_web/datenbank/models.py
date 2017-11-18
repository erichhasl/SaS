from django.db import models


# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('Veröffentlichungsdatum')
    image = models.ImageField('Vorschaubild', upload_to='thumbnails')
    element = models.FileField('Datei', upload_to='datastorage')
