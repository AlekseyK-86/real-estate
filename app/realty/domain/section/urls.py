from django.urls import path
from .views import SectionListView, SectionDetailView

urlpatterns = [
    path('', SectionListView.as_view()),
    path('<int:section_id>/', SectionDetailView.as_view())
]
