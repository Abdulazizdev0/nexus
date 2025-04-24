from django.urls import path
from .views import CbvApiUser,BlogDetailView

urlpatterns = [
    path('',CbvApiUser.as_view()),
    path('<int:pk>/',BlogDetailView.as_view())
]
