from django.urls import path
from .views import get_codeforces_user, get_contest_leaderboard

urlpatterns = [
    path('user/<str:username>/', get_codeforces_user, name="codeforces-user"),
    path('contest/<int:contest_id>/', get_contest_leaderboard, name="contest-leaderboard"),
]
