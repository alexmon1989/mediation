from django.urls import path
from .views import index, send_email


app_name = 'contacts'
urlpatterns = [
    path('', index, name="index"),
    path('send-email', send_email, name="send_email"),
]
