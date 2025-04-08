from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from datetime import timedelta
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Removed MongoDB-specific code as we are now using SQLite
        # No need to connect to MongoDB or drop collections

        # Clear all objects in SQLite database
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Use get_or_create to avoid duplicate User entries
        users = [
            User.objects.get_or_create(email='thundergod@octofit.edu', defaults={'name': 'Thundergod', 'password': 'thundergodpassword'})[0],
            User.objects.get_or_create(email='metalgeek@octofit.edu', defaults={'name': 'Metalgeek', 'password': 'metalgeekpassword'})[0],
            User.objects.get_or_create(email='zerocool@octofit.edu', defaults={'name': 'Zerocool', 'password': 'zerocoolpassword'})[0],
            User.objects.get_or_create(email='crashoverride@octofit.edu', defaults={'name': 'Crashoverride', 'password': 'crashoverridepassword'})[0],
            User.objects.get_or_create(email='sleeptoken@octofit.edu', defaults={'name': 'Sleeptoken', 'password': 'sleeptokenpassword'})[0],
        ]

        # Explicitly save all User objects to ensure they are properly initialized
        for user in users:
            user.save()

        # Create teams
        teams = [
            Team(name='Blue Team', members=[]),
            Team(name='Gold Team', members=[])
        ]

        # Save teams individually to ensure compatibility with SQLite
        for team in teams:
            team.save()

        # Ensure user field in Activity is assigned valid User instances
        activities = [
            Activity(user=User.objects.get(email='thundergod@octofit.edu'), type='Cycling', duration=60, date='2025-04-01'),
            Activity(user=User.objects.get(email='metalgeek@octofit.edu'), type='Crossfit', duration=120, date='2025-04-02'),
            Activity(user=User.objects.get(email='zerocool@octofit.edu'), type='Running', duration=90, date='2025-04-03'),
            Activity(user=User.objects.get(email='crashoverride@octofit.edu'), type='Strength', duration=30, date='2025-04-04'),
            Activity(user=User.objects.get(email='sleeptoken@octofit.edu'), type='Swimming', duration=75, date='2025-04-05'),
        ]

        # Save activities individually to ensure related user objects are properly associated
        for activity in activities:
            activity.save()

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(team=teams[0], score=100),
            Leaderboard(team=teams[1], score=90),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event'),
            Workout(name='Crossfit', description='Training for a crossfit competition'),
            Workout(name='Running Training', description='Training for a marathon'),
            Workout(name='Strength Training', description='Training for strength'),
            Workout(name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))