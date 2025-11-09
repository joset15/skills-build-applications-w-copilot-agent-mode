from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_user_creation(self):
        user = User.objects.create(name='Test User', email='test@example.com', team='test')
        self.assertEqual(user.name, 'Test User')
    def test_team_creation(self):
        team = Team.objects.create(name='test', members=['Test User'])
        self.assertEqual(team.name, 'test')
    def test_activity_creation(self):
        activity = Activity.objects.create(user='Test User', activity='Running', duration=30)
        self.assertEqual(activity.activity, 'Running')
    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(team='test', points=100)
        self.assertEqual(leaderboard.points, 100)
    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', description='Test Desc')
        self.assertEqual(workout.name, 'Test Workout')
