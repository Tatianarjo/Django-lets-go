from django.db import models
# from levelupapi.models import Gamer
# from levelupapi.models import Game


class Event(models.Model):

    description = models.CharField(max_length=100)
    date = models.DateTimeField ()
    maker = models.ForeignKey("levelupapi.Gamer", on_delete=models.DO_NOTHING)
    game = models.ForeignKey("levelupapi.Game", on_delete=models.CASCADE)
    time = models.TimeField(null=True)