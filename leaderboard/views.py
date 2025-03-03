from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Participant
from .serializers import ParticipantSerializer
from .utils import fetch_codeforces_user_details

# ✅ Codeforces User Rating Fetch Karna
@api_view(['GET'])
def get_codeforces_user(request, username):
    user_data = fetch_codeforces_user_details(username)
    if user_data:
        return Response(user_data)
    return Response({"error": "User not found"}, status=404)

# ✅ Contest ke baad Leaderboard Generate Karna
@api_view(['GET'])
def get_contest_leaderboard(request, contest_id):
    participants = Participant.objects.filter(contest_id=contest_id).order_by('-score')

    # ✅ Rank Assign Karna
    rank = 1
    for participant in participants:
        participant.rank = rank
        participant.save()
        rank += 1

    serializer = ParticipantSerializer(participants, many=True)
    return Response(serializer.data)
