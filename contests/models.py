from django.db import models
from django.conf import settings  # Custom User Model ke liye

class Question(models.Model):
    contest_id = models.IntegerField()  # Codeforces contest ID
    index = models.CharField(max_length=10)  # Problem index (A, B, C, etc.)
    name = models.CharField(max_length=255)  # Problem title
    rating = models.IntegerField(null=True, blank=True)  # Problem difficulty rating
    tags = models.JSONField(default=list)  # List of tags

    def __str__(self):
        return f"{self.contest_id}{self.index} - {self.name}"

class Contest(models.Model):
    name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question, blank=True)  # Many-to-Many relation

    def __str__(self):
        return self.name
