from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings  # Custom User Model ke liye
from contests.models import Contest

class Participant(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    codeforces_username = models.CharField(max_length=50)  # ✅ User ka Codeforces username
    score = models.IntegerField(default=0)  # ✅ Contest me mila score
    rank = models.IntegerField(null=True, blank=True)  # ✅ Leaderboard rank

    def __str__(self):
        return f"{self.user.username} - {self.contest.name}"

