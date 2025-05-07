from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Users
        users = [
            {"_id": ObjectId(), "username": "superman", "email": "superman@octofit.com", "password": "krypton"},
            {"_id": ObjectId(), "username": "wonderwoman", "email": "wonderwoman@octofit.com", "password": "themyscira"},
            {"_id": ObjectId(), "username": "batman", "email": "batman@octofit.com", "password": "wayne"},
        ]
        db.users.insert_many(users)

        # Teams
        teams = [
            {"_id": ObjectId(), "name": "Justice League", "members": [users[0]["_id"], users[1]["_id"]]},
            {"_id": ObjectId(), "name": "Gotham Knights", "members": [users[2]["_id"]]},
        ]
        db.teams.insert_many(teams)


        # Activities (store duration as integer minutes for BSON compatibility)
        try:
            activities = [
                {"_id": ObjectId(), "user": users[0]["_id"], "activity_type": "run", "duration": 30},
                {"_id": ObjectId(), "user": users[1]["_id"], "activity_type": "walk", "duration": 45},
                {"_id": ObjectId(), "user": users[2]["_id"], "activity_type": "strength", "duration": 60},
            ]
            db.activity.insert_many(activities)
            self.stdout.write(self.style.SUCCESS('Activities insérées'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Erreur insertion activities: {e}'))

        try:
            leaderboard = [
                {"_id": ObjectId(), "user": users[0]["_id"], "score": 150},
                {"_id": ObjectId(), "user": users[1]["_id"], "score": 120},
                {"_id": ObjectId(), "user": users[2]["_id"], "score": 180},
            ]
            db.leaderboard.insert_many(leaderboard)
            self.stdout.write(self.style.SUCCESS('Leaderboard inséré'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Erreur insertion leaderboard: {e}'))

        try:
            workouts = [
                {"_id": ObjectId(), "name": "Pushups", "description": "Do 20 pushups"},
                {"_id": ObjectId(), "name": "Situps", "description": "Do 30 situps"},
                {"_id": ObjectId(), "name": "Squats", "description": "Do 40 squats"},
            ]
            db.workouts.insert_many(workouts)
            self.stdout.write(self.style.SUCCESS('Workouts insérés'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Erreur insertion workouts: {e}'))

        self.stdout.write(self.style.SUCCESS('Test data successfully populated in octofit_db.'))
