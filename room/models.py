from django.db import models
from django.conf import settings
# Create your models here.
class Rooms(models.Model):
    ROOM_CATEGORIES = (
        ('SC', 'SELF CONTAINED'),
        ('SR', 'SINGLE ROOM'),
        ('DB', 'DORMITORY BUNKS'),
        
        
    )
    rooms = models.IntegerField(null=True, blank=True)
    category = models.CharField(max_length=2, choices=ROOM_CATEGORIES)
    beds = models.IntegerField()
    capacity = models.IntegerField(null=True, blank=True)
    

    def __str__(self):
        return f'room {self.rooms} {self.category} with {self.beds} bed'

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.check_in} to {self.check_out}'