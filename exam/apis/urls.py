from .views import get
from django.urls import path

urlpatterns = [
    path('get/',get.home_view.as_view(), name='home'),
    path('get/<int:exam_id>/',get.exam_view.as_view(), name='exam_view'),
]