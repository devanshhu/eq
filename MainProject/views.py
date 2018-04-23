from django.shortcuts import render
from django.http import HttpResponse
import pyqrcode
from django.utils import timezone
import MySQLdb
from .models import AppUser
from .forms import UserForm
from datetime import timedelta, datetime

# from django.template.loader import get_template
# Create your views here.


def qrview(request):
    now = datetime.now().strftime('%y-%m-%d')
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
            instance.timestamp = timezone.now()
            instance.regdate = timezone.now()
            lastregdate = AppUser.objects.all().order_by("-timestamp")[:1]

            if lastregdate[0].regdate == timezone.now().date():
                lastslot = AppUser.objects.all().order_by("-timeslot_end")[:1]
                if lastslot[0].timeslot_end:
                    nexttimeslotStart = lastslot[0].timeslot_end
                else:
                    nexttimeslotStart = timezone.now()
                # print("insode if")
            else:
                nexttimeslotStart = timezone.now() + timedelta(minutes=5)
                # print("inside else")
            instance.timeslot_start = nexttimeslotStart
            instance.timeslot_end = nexttimeslotStart + timedelta(minutes=30)
            instance.save()
            # details = form.cleaned_data['detailforappointment']
            return HttpResponse("Thanx for Registering ")
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
    if query:

        listofpeople = query.filter(regdate=timezone.now())
        if not listofpeople.exists():
            context = {
                "queue": '',
            }
            return HttpResponse("No Result Found For Today")
        context = {
            "queue": listofpeople,
        }
        return render(request, 'list.html', context)
    else:
        listofpeople = 'Nothing To Show'
        context = {
            "queue": listofpeople,
        }
        return render(request, 'NoList.html', context)
