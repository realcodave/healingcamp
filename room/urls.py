from django.urls import path
from .views import RoomList, BookingList, BookingView, HomeTemplateView, ContactTemplateView, ServicesTemplateView


urlpatterns = [
    path("", HomeTemplateView.as_view(), name='home'),
    path("contact/", ContactTemplateView.as_view(), name='contact'),
    path("service/", ServicesTemplateView.as_view(), name='service'),
    path("room_list/", RoomList.as_view(), name='RoomList'),
    path("booking_list/", BookingList.as_view(), name='BookingList'),
    path('book/', BookingView.as_view(), name='booking_view')
]