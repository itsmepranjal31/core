import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Contest, Question
from .serializers import ContestSerializer, QuestionSerializer

# ✅ 1️⃣ Codeforces API se problems fetch karna
@api_view(['GET'])
def get_codeforces_questions(request):
    url = "https://codeforces.com/api/problemset.problems"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data["status"] == "OK":
            problems = data["result"]["problems"]

            # ✅ Questions ko DB me save karne ka logic
            for problem in problems:
                Question.objects.update_or_create(
                    contest_id=problem["contestId"],
                    index=problem["index"],
                    defaults={
                        "name": problem["name"],
                        "rating": problem.get("rating", None),
                        "tags": problem.get("tags", [])
                    }
                )

            return Response(problems)  # ✅ Frontend ke liye JSON response
    return Response({"error": "Failed to fetch problems"}, status=500)

# ✅ 2️⃣ Contest List & Creation API
class ContestListCreateView(generics.ListCreateAPIView):
    queryset = Contest.objects.all()
    serializer_class = ContestSerializer
    permission_classes = [IsAuthenticated]

# ✅ 3️⃣ Contest Detail API
class ContestDetailView(generics.RetrieveAPIView):
    queryset = Contest.objects.all()
    serializer_class = ContestSerializer
    permission_classes = [IsAuthenticated]
