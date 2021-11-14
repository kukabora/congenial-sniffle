from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CustomUser(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="customUser")
    phone = models.CharField(max_length=50, null=False)
    balance = models.IntegerField(default=0)


class Team(models.Model):
    name = models.CharField(max_length=40, null=False)
    wins = models.IntegerField(name="amount_of_wins", default=0)
    loses = models.IntegerField(name="amount_of_loses", default=0)


class Category(models.Model):
    name = models.CharField(max_length=50, name="name_of_category")


class Outcome(models.Model):
    name = models.CharField(max_length=50, null=False)


class Match(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    first_team = models.ForeignKey(
        Team, related_name="match+", on_delete=models.CASCADE, default=5)
    second_team = models.ForeignKey(
        Team, related_name="match+", on_delete=models.CASCADE, default=5)
    location = models.CharField(
        name="location_of_match", null=False, max_length=50)
    group = models.CharField(name="tournament_name", null=False, max_length=50)


class Bet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    match_id = models.ForeignKey(Match, on_delete=models.CASCADE)
    bet = models.IntegerField(null=False)
    outcome = models.ForeignKey(Outcome, on_delete=models.CASCADE)
