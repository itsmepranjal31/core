import requests

def fetch_codeforces_user_details(username):
    url = f"https://codeforces.com/api/user.info?handles={username}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data["status"] == "OK":
            user_info = data["result"][0]
            return {
                "username": user_info["handle"],
                "rating": user_info.get("rating", "N/A"),
                "rank": user_info.get("rank", "N/A"),
                "max_rating": user_info.get("maxRating", "N/A"),
                "max_rank": user_info.get("maxRank", "N/A"),
                "avatar": user_info.get("avatar", ""),
            }
    return None
