import datetime

from django.db import models

# Create your models here.
class Blogs(models.Model):
    title=models.CharField(max_length=70)
    desc=models.TextField()
    date=models.DateField(default=datetime.date.today)


    def __str__(self):
        return self.title
