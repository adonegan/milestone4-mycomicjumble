from django.db import models


class Comic(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    grade = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.name
