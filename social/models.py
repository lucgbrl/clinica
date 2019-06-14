from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length = 256)

    def __str__(self):
        return self.title
