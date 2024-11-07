from django.urls import path

from .views import FlatListView, FlatDetailView

urlpatterns = [
    path('', FlatListView.as_view(), name='flats'),
    path('<int:flat_id>/', FlatDetailView.as_view(), name='flat_detail')
]