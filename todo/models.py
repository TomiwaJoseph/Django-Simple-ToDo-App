from django.db import models

# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task