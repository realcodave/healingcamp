from django.db import models

# Create your models here.
class Rooms(models.Model):
    ROOM_CATEGORIES = (
        ('SC', 'SELF CONTAINED'),
        ('SR', 'SINGLE ROOM'),
        ('DB', 'DORMITORY BUNKS'),
        
        
    )
    rooms = models.IntegerField()
    category = models.CharField(max_length=2, choices=ROOM_CATEGORIES)
    beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.rooms} {self.category} with {self.beds} for {self.capacity} person(s)'

