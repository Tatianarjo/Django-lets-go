from django.db import models
# from levelupapi.models import Gamer 



class Game(models.Model):

    name = models.CharField(max_length=50)
    player_limit = models.IntegerField()
    gametype = models.ForeignKey("levelupapi.gametype", on_delete=models.SET_NULL, null=True)