from django.db import models


class Books(models.Model):

    title = models.CharField(max_length=25)
    pyblish_year = models.IntegerField()
    is_bestseller = models.BooleanField()
