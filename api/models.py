from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    content = models.CharField(max_length=140, null=True)
    time = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return f"/task/{self.id}"