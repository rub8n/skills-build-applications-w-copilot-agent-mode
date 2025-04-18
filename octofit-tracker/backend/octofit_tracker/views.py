from rest_framework import viewsets
from rest_framework.response import Response
from django.http import JsonResponse
from django.conf import settings
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

def get_codespace_url():
    return "https://potential-fortnight-r444jqx5gr53vj5-8000.app.github.dev"

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({
            'codespace_url': get_codespace_url(),
            'data': response.data
        })

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({
            'codespace_url': get_codespace_url(),
            'data': response.data
        })

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response(response.data)  # Return serialized data directly

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({
            'codespace_url': get_codespace_url(),
            'data': response.data
        })

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({
            'codespace_url': get_codespace_url(),
            'data': response.data
        })