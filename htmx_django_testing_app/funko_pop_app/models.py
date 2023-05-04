from django.db import models

from model_utils import Choices


class FunkoPop(models.Model):
    name = models.CharField(max_length=255, blank=False)
    number = models.PositiveIntegerField(blank=False)
    LINE = Choices(
        (1, 'dc', 'DC'),
        (2, 'marvel', 'MARVEL'),
        (3, 'star_wars', 'STAR WARS'),
        (4, 'animation', 'ANIMATION'),
        (5, 'games', 'GAMES'),
    )
    line = models.PositiveSmallIntegerField(choices=LINE, blank=False)
    production_date = models.DateField()
    is_vaulted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.number}-{self.name}-{self.line}"
