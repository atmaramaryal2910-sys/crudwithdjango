from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    team = models.CharField(max_length=100)
    age = models.IntegerField()
    nationality = models.CharField(max_length=100)
    image = models.ImageField(upload_to='player_photos/', null=True, blank=True)

    def __str__(self):
        return self.name
