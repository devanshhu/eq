from django.shortcuts import render
from django.http import HttpResponse
import pyqrcode
from django.utils import timezone
import MySQLdb
from .models import AppUser
from .forms import UserForm
import datetime
# from django.template.loader import get_template
# Create your views here.


def qrview(request):
    now = datetime.datetime.now().strftime('%y-%m-%d')
    svg = pyqrcode.create('http://localhost:8000/register-' + now)
    svg.svg('MainProject/static/qrcode.svg', scale=8)
    # t = get_template('QR.html')
    context = {

    }
    # html = t.render(context)
    return render(request, "QR.html", context)


def registerUser(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=True)
            instance.user = request.user
            # print(instance.course)
            instance.timestamp = datetime.datetime.now()
            instance.timeslot_start = timezone.now()
            instance.regdate = timezone.now

            instance.save()
            name = form.cleaned_data['name']
            year = form.cleaned_data['year']
            rollno = form.cleaned_data['enrollmentno']
            course = form.cleaned_data['course']

            details = form.cleaned_data['detailforappointment']
            return HttpResponse(" Thanx for Registering ")
        else:
            print("Entered Else")
    else:
        form = UserForm()
    context = {
        "form": form
    }

    return render(request, 'post_form.html', context)


def listView(request):
    query = AppUser.objects.all().order_by("-id")
    # print('inside list')
    if query:
        # print('result found->')
        listofpeople = query.filter(regdate=timezone.now())
        context = {
            "queue": query,
        }
        # print(listofpeople)
        return render(request, 'list.html', context)
