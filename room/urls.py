from django.urls import path
from .views import HomeTemplateView, ContactTemplateView, ServicesTemplateView

urlpatterns = [
    path("", HomeTemplateView.as_view(), name='home'),
    path("contact/", ContactTemplateView.as_view(), name='contact'),
    path("service/", ServicesTemplateView.as_view(), name='service')
]