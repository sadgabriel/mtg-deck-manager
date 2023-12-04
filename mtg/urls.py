from django.urls import path
from . import views

app_name = 'mtg'

urlpatterns = [
    path('', views.root, name='root'),
    path('login', views.login, name='login'),
    path('<str:username>/home', views.home, name='home'),
    path('<str:username>/home/<str:deckname>', views.deck, name='deck')
]