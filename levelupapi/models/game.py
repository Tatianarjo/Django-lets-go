from django.db import models
# from levelupapi.models import Gamer 



class Game(models.Model):

    name = models.CharField(max_length=50)
    player_limit = models.IntegerField()
    gamer = models.ForeignKey("levelupapi.Gamer", on_delete=models.DO_NOTHING)