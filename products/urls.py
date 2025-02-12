from django.urls import path

from . import views

urlpatterns = [
    path("", views.FoodListAPIView.as_view()),
]
