from django.db import models

POSITION_CHOICES = [
    ('Goalkeeper', 'Goalkeeper'),
    ('Sweeper', 'Sweeper'),
    ('Centre-back', 'Centre-back'),
    ('Full-back', 'Full-back'),
    ('Wing-back', 'Wing-back'),
    ('Defensive Midfielder', 'Defensive Midfielder'),
    ('Central Midfielder', 'Central Midfielder'),
    ('Attacking Midfielder', 'Attacking Midfielder'),
    ('Winger', 'Winger'),
    ('Forward', 'Forward'),
    ('Striker', 'Striker'),
]

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50, choices=POSITION_CHOICES)
    team = models.CharField(max_length=100)
    age = models.IntegerField()
    nationality = models.CharField(max_length=100)
    image = models.ImageField(upload_to='player_photos/', null=True, blank=True)

    def __str__(self):
        return self.name
