from django.shortcuts import render, redirect
from django.core.mail import send_mail
from Portfolio import settings
from .models import *
from .forms import *

# Create your views here.
def index(request):

    # Send Message
    if request.method == "POST":
        mess = SendForm(request.POST)
        if mess.is_valid():
            mess.save()

            # Send Message in mail
            # subb = request.POST['sub']
            # mssg = request.POST['msg']
            # f_id = (settings.EMAIL_HOST_USER)
            # t_id =[request.POST['email']]
            # send_mail(subject=subb, message=mssg, from_email=f_id, recipient_list=t_id)
            return redirect('thanks')
        else:
            print(mess.errors)

    return render(request, 'index.html')

def thanks(request):
    return render(request, 'thanks.html')