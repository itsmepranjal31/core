from rest_framework import serializers
from .models import Profile
import requests

class ProfileSerializer(serializers.ModelSerializer):
    codeforces_profile = serializers.SerializerMethodField()  # ✅ Fetch Codeforces data

    class Meta:
        model = Profile
        fields = [
            "user", "codeforces_username", "bio", "avatar",
            "current_rating", "total_questions_solved", "contests_participated",
            "codeforces_profile"  # ✅ Include Codeforces profile data
        ]

    def get_codeforces_profile(self, obj):
        """ Fetch live Codeforces data for the user """
        if not obj.codeforces_username:
            return None  # ✅ No Codeforces username

        cf_url = f"https://codeforces.com/api/user.info?handles={obj.codeforces_username}"
        cf_response = requests.get(cf_url)

        if cf_response.status_code == 200:
            cf_data = cf_response.json()
            if "result" in cf_data:
                cf_user = cf_data["result"][0]
                return {
                    "handle": cf_user["handle"],
                    "rating": cf_user.get("rating", "N/A"),
                    "maxRating": cf_user.get("maxRating", "N/A"),
                    "rank": cf_user.get("rank", "N/A"),
                    "maxRank": cf_user.get("maxRank", "N/A"),
                    "avatar": cf_user.get("avatar", ""),
                }
        return {"error": "Failed to fetch Codeforces data"}
