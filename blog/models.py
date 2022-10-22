from django.db import models

class Blog(models.Model):
    objects = None
    title = models.CharField(max_length=200, blank = True)
    description = models.TextField()
    data = models.DateField()

    def __str__(self):
        return self.title