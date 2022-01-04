from django.db import models
# from levelupapi.models import Gamer 



class GameType(models.Model):

    label = models.CharField(max_length=50)

    