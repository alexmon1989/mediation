from django.urls import path
from .views import ResourceListView, ResourceDetailView


app_name = 'resources'
urlpatterns = [
    path('', ResourceListView.as_view(), name="index"),
    path('detail/<slug:slug>/', ResourceDetailView.as_view(), name="detail"),
]
