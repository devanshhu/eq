from django.shortcuts import render
from django.http import HttpResponse
import pyqrcode
from .models import AppUser
from .forms import UserForm
import datetime
# from django.template.loader import get_template
# Create your views here.


def qrview(request):
    dt = datetime.datetime.now().strftime('%y-%m-%d')
    svg = pyqrcode.create('http://localhost:8000/register-' + now)
    svg.svg('MainProject/static/qrcode.svg', scale=8)
    # t = get_template('QR.html')
    context = {

    }
    # html = t.render(context)
    return render(request, "QR.html", context)


def registerUser(request):
    form = UserForm()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Registered Successfully ")
        return HttResponse(" Thanx for Registering ")

    context = {
        "form": form
    }

    return render(request, 'post_form.html', context)
