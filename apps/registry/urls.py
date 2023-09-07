from django.urls import path
from .views import MediatorListView, MediatorDetailView


app_name = 'registry'
urlpatterns = [
    path('', MediatorListView.as_view(), name="index"),
    path('detail/<int:pk>/', MediatorDetailView.as_view(), name="detail"),
]
