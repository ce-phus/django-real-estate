from django.urls import path

from .views import (AgentListAPIView, GetProfileAPIView, TopAgentssListAPIView,
                    UpdateProfileAPIView)

urlpatterns= [
    path("me/", GetProfileAPIView.as_view(), name="get-profile"),
    path("update/<str:username>/", UpdateProfileAPIView.as_view(), name="update-profile"),
    path("agents/all/", AgentListAPIView.as_view(), name="all-agents"),
    path("top-agents/all", TopAgentssListAPIView.as_view(), name="top-agents"),
]