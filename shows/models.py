from django.db import models


class TCShow(models.Model):
    GENRE_CHOISE = (
        ('Detective', 'Detective'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Horror', 'Horror'),
    )
    tittle = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    quantity = models.IntegerField()
    qenre = models.CharField(choices=GENRE_CHOISE, max_length=100)
    date_filmed = models.DateField()

