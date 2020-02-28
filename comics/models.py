from django.db import models

# Comic model with all information fields in database


class Comic(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    condition = models.CharField(max_length=200)
    grade = models.CharField(max_length=20)
    penciler = models.CharField(max_length=50)
    cover_artist = models.CharField(max_length=50)
    brand = models.CharField(max_length=30, blank=True, null=True)
    writer = models.CharField(max_length=30, blank=True, null=True)
    published_date = models.DateField(blank=True, null=True, auto_now=False)

    def __str__(self):
        return self.name
