from django.db import models


class Item(models.Model):
    """To do item to show"""
    title = models.CharField(max_length=255, unique=True)
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
