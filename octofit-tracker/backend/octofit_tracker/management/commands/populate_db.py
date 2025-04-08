from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            User(email='thundergod@octofit.edu', name='Thundergod', password='thundergodpassword'),
            User(email='metalgeek@octofit.edu', name='Metalgeek', password='metalgeekpassword'),
            User(email='zerocool@octofit.edu', name='Zerocool', password='zerocoolpassword'),
            User(email='crashoverride@octofit.edu', name='Crashoverride', password='crashoverridepassword'),
            User(email='sleeptoken@octofit.edu', name='Sleeptoken', password='sleeptokenpassword'),
        ]

        # Save users individually to ensure they are persisted in the database
        for user in users:
            user.save()

        # Create teams
        teams = [
            Team(name='Blue Team', members=[]),
            Team(name='Gold Team', members=[])
        ]
        Team.objects.bulk_create(teams)

        # Create activities
        activities = [
            Activity(user=users[0], type='Cycling', duration=60, date='2025-04-01'),
            Activity(user=users[1], type='Crossfit', duration=120, date='2025-04-02'),
            Activity(user=users[2], type='Running', duration=90, date='2025-04-03'),
            Activity(user=users[3], type='Strength', duration=30, date='2025-04-04'),
            Activity(user=users[4], type='Swimming', duration=75, date='2025-04-05'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), user=users[0], score=100),
            Leaderboard(_id=ObjectId(), user=users[1], score=90),
            Leaderboard(_id=ObjectId(), user=users[2], score=95),
            Leaderboard(_id=ObjectId(), user=users[3], score=85),
            Leaderboard(_id=ObjectId(), user=users[4], score=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), name='Cycling Training', description='Training for a road cycling event'),
            Workout(_id=ObjectId(), name='Crossfit', description='Training for a crossfit competition'),
            Workout(_id=ObjectId(), name='Running Training', description='Training for a marathon'),
            Workout(_id=ObjectId(), name='Strength Training', description='Training for strength'),
            Workout(_id=ObjectId(), name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))