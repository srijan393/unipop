from django.db import models

class Room(models.Model):
    number = models.CharField(max_length=8)
    building = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.building} - {self.number}"


from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=64, unique=True)  # Add unique constraint
    dean = models.CharField(max_length=64, null=True)

    def __str__(self):
        return self.name
