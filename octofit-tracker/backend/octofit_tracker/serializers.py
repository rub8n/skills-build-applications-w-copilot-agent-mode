from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.name', read_only=True)  # Include user's name

    class Meta:
        model = Activity
        fields = '__all__'

class LeaderboardSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(source='team.name', read_only=True)  # Include team name

    class Meta:
        model = Leaderboard
        fields = ['id', 'team_name', 'score']  # Explicitly define fields to include team name

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'