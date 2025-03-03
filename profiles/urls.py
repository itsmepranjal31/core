from django.urls import path
from .views import ProfileDetailView  # ✅ Only import ProfileDetailView

urlpatterns = [
    path('<int:pk>/', ProfileDetailView.as_view(), name="profile-detail"),  # ✅ GET /profiles/1/
]
