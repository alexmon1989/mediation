from django.urls import path
from .views import cases_count


app_name = 'cases'
urlpatterns = [
    path('cases-count/<int:mediator_pk>/', cases_count, name="count"),
]
