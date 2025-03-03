from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    codeforces_username = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    avatar = models.URLField(blank=True, null=True)
    current_rating = models.IntegerField(default=0)
    total_questions_solved = models.IntegerField(default=0)
    contests_participated = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.codeforces_username}"
