from django.db import models
# from levelupapi.models import Gamer 



class Game(models.Model):

    title = models.CharField(max_length=50)
    maker = models.CharField(max_length=300)
    gamer = models.ForeignKey("levelupapi.Gamer", on_delete=models.DO_NOTHING)
    game_type = models.ForeignKey("levelupapi.gametype", on_delete=models.SET_NULL, null=True)
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField(default=1)


##make these match your games.json file t
##  Then make migration then migrate then load data again
## migrate event and game

##  Add or change a related_name argument to the definition for 'levelupapi.Game.maker' or 'levelupapi.Game.gamer'