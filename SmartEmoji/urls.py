from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='home'),
    path('choose_emoji', views.choose_emoji, name='choose_emoji'),
    path('emoji_books', views.emoji_books, name='emoji_books'),
]
