from django.db import models


class Comic(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    condition = models.CharField(max_length=200)
    grade = models.CharField(max_length=20)
    penciler = models.CharField(max_length=50)
    cover_artist = models.CharField(max_length=50)

    def __str__(self):
        return self.name
