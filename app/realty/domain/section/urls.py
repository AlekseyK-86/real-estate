from django.urls import path

from .views import SectionListView, SectionDetailView

urlpatterns = [
    path('', SectionListView.as_view()),
    path('<int:pk>/', SectionDetailView.as_view())
]
