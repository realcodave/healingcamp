from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage
from django.conf import settings 
# Create your views here.
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
