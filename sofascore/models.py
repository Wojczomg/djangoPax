from django.db import models



class LiveTable(models.Model):
    customId = models.CharField(max_length=20)
    slug = models.CharField(max_length=20)
    event_id = models.CharField(max_length=20,unique=True)
    formatedStartDate = models.CharField(max_length=20)
    homeTeam_name = models.CharField(max_length=20)
    awayTeam_name = models.CharField(max_length=20)
    current_home = models.IntegerField()
    current_away = models.IntegerField()
    period1_home = models.IntegerField()
    period1_away = models.IntegerField()
    period2_home = models.IntegerField()
    period2_away = models.IntegerField()
    period3_home = models.IntegerField()
    period3_away = models.IntegerField()
    odds_home = models.FloatField(blank=True,null=True)
    odds_away = models.FloatField(blank=True,null=True)
    tennis_ssmg = models.FloatField(blank=True,null=True)
    


