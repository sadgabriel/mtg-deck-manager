from django.contrib import admin
from . import models

admin.site.register(models.User)
admin.site.register(models.Card)
admin.site.register(models.Deck)
admin.site.register(models.Contain)