from django.db import models

class Room(models.Model):
    BUILDINGS = [
        ('Leighton', 'Leighton'),
        ('Priestley', 'Priestley'),
    ]

    number = models.CharField(max_length=8)
    building = models.CharField(
        max_length=12,
        choices=BUILDINGS,
    )

    class Meta:
        ordering = ['building', 'number']
        unique_together = ['number', 'building']

    def __str__(self):
        return f'Room {self.number}, {self.building} Building'

from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=64, unique=True)
    dean = models.CharField(max_length=64, null=True)

    class Meta:
        verbose_name_plural = 'Faculties'
        ordering = ['name']

    def __str__(self):
        return self.name


from django.db import models

class Tutor(models.Model):
    surname = models.CharField(max_length=64)
    forenames = models.CharField(max_length=64)
    email = models.EmailField(null=True)

    faculty = models.ForeignKey(Faculty, null=True, on_delete=models.SET_NULL)
    room = models.ForeignKey(Room, null=True, on_delete=models.SET_NULL)

    # New fields for created and updated timestamps
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = [
            'surname',
            'forenames',
        ]

    def __str__(self):
        return f'{self.forenames} {self.surname}'
