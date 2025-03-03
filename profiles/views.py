import requests
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer

class ProfileDetailView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        profile = self.get_object()  # Get profile from database
        serialized_profile = self.get_serializer(profile).data  # Serialize profile

        # ✅ Fetch Codeforces user info
        codeforces_username = profile.codeforces_username
        if codeforces_username:
            cf_url = f"https://codeforces.com/api/user.info?handles={codeforces_username}"
            cf_response = requests.get(cf_url)

            if cf_response.status_code == 200:
                cf_data = cf_response.json()
                if "result" in cf_data:
                    cf_user = cf_data["result"][0]
                    serialized_profile["codeforces_profile"] = {
                        "handle": cf_user["handle"],
                        "rating": cf_user.get("rating", "N/A"),
                        "maxRating": cf_user.get("maxRating", "N/A"),
                        "rank": cf_user.get("rank", "N/A"),
                        "maxRank": cf_user.get("maxRank", "N/A"),
                        "avatar": cf_user.get("avatar", ""),
                    }

            # ✅ Fetch past contests and rating changes
            contest_url = f"https://codeforces.com/api/user.rating?handle={codeforces_username}"
            contest_response = requests.get(contest_url)

            if contest_response.status_code == 200:
                contest_data = contest_response.json()
                if "result" in contest_data:
                    past_contests = [
                        {
                            "contestId": c["contestId"],
                            "contestName": c.get("contestName", "N/A"),
                            "rank": c["rank"],
                            "ratingChange": c["newRating"] - c["oldRating"],
                            "newRating": c["newRating"]
                        }
                        for c in contest_data["result"]
                    ]
                    serialized_profile["past_contests"] = past_contests
            else:
                serialized_profile["past_contests"] = {"error": "Failed to fetch contest history"}

        return Response(serialized_profile)
