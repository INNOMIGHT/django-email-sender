from django.urls import path
from .views import send_mail

urlpatterns = [
    path('contact', send_mail, name="contact")
]
