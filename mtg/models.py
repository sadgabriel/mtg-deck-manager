from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    is_superuser = models.BooleanField()
    
    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'user'
        

class Card(models.Model):
    name = models.CharField(max_length=50, unique=True)
    cost = models.CharField(max_length=10)
    type = models.CharField(max_length=50)
    text = models.CharField(max_length=200, null=True)
    power = models.IntegerField(null=True)
    toughness = models.IntegerField(null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'card'


class Deck(models.Model):
    deckname = models.CharField(max_length=50, unique=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username', db_column='username')
    
    def __str__(self):
        return self.deckname
    
    class Meta:
        db_table = 'deck'


class Contain(models.Model):
    deckname = models.ForeignKey(Deck, on_delete=models.CASCADE, to_field='deckname', db_column='deckname')
    cardname = models.ForeignKey(Card, on_delete=models.CASCADE, to_field='name', db_column='cardname')
    number = models.IntegerField()
    
    class Meta:
        db_table = 'contain'
    

    
        