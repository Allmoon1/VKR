from django.db import models


class User(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)

    def __str__():
        return self.username


# Create your models here.

