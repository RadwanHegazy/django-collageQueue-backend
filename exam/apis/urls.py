from .views import get, patch
from django.urls import path

urlpatterns = [
    path('get/',get.home_view.as_view(), name='home'),
    path('get/<int:exam_id>/',get.exam_view.as_view(), name='exam_view'),
    path('section/pending/<int:section_id>/',patch.section_pending.as_view(), name='section_pending'),
    path('section/done/<int:section_id>/',patch.section_done.as_view(), name='section_done'),
]