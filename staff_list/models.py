from django.db import models

class Room(models.Model):
    number = models.CharField(max_length=8)
    building = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.building} - {self.number}"


class Faculty(models.Model):
    name = models.CharField(max_length=64)
    dean = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return self.name
