from django.urls import path
from .views import get_codeforces_questions, ContestListCreateView, ContestDetailView

urlpatterns = [
    path('codeforces-problems/', get_codeforces_questions, name="codeforces-problems"),
    path('', ContestListCreateView.as_view(), name="contest-list-create"),
    path('<int:pk>/', ContestDetailView.as_view(), name="contest-detail"),
]
