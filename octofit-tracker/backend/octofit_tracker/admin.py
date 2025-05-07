from django.contrib import admin
from django.urls import path

# Register your models here for admin interface
from .models import User, Team, Activity, Leaderboard, Workout
from django.contrib import admin

admin.site.register(User)
admin.site.register(Team)
admin.site.register(Activity)
admin.site.register(Leaderboard)
admin.site.register(Workout)
