from django.db import models

# Create your models here.
class user(models.Model):
    username=models.CharField(primary_key=True,max_length=50)
    password=models.CharField(max_length=30)

    def __str__(self):
        return self.username or ''