from django.db import models

class DatabaseTable(models.Model):
    name = models.CharField(max_length=100, unique=True)
    columns_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
