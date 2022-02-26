from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, FormView
from django.core.mail import EmailMessage
from django.conf import settings 
from .models import Rooms, Booking
from .forms import AvailabilityForm
from room.booking_funtion.availability import check_availability
# Create your views here.

class RoomList(ListView):
    model = Rooms

class BookingList(ListView):
    model = Booking

class BookingView(FormView):
    form_class = AvailabilityForm
    template_name = 'room/availability_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        room_list = Rooms.objects.filter(category=data['room_category'])
        available_rooms = []
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)
        if len(available_rooms) > 0:

            room = available_rooms[0]
            booking = Booking.objects.create(
                user = self.request.user,
                room = room,
                check_in = data['check_in'],
                check_out = data['check_out'],
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('This category of rooms are booked!! Try another ')


class HomeTemplateView(TemplateView):
    template_name = 'index.html'


class ContactTemplateView(TemplateView):
    template_name = 'contact.html'

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        email = EmailMessage(
            subject = f"{name} from Healing Camp",
            body = message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email] 
        )
        email.send()
        return HttpResponse("Email sent successfully")
        

class ServicesTemplateView(TemplateView):
    template_name = 'service.html'
