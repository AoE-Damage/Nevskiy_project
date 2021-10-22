from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.


def mainpage(request):
    if request.method == "POST":
        zayavka = zayavki()
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        phone_number = request.POST.get("phone_number")
        zayavka.name = name
        zayavka.surname = surname
        zayavka.phone_number = phone_number
        zayavka.save()

        return render(request, "kv/main.html")
    ###

    return render(request, "kv/main.html")


def home(request):

    if request.method == "POST":
        zayavka = zayavki()
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        phone_number = request.POST.get("phone_number")
        zayavka.name = name
        zayavka.surname = surname
        zayavka.phone_number = phone_number
        zayavka.save()

        return render(request, "kv/main.html")
    # homes = apartments.objects.all()
    parkings = parking.objects.all()
    floor3 = apartments.objects.filter(floor="3")
    floor4 = apartments.objects.filter(floor="4")
    floor5 = apartments.objects.filter(floor="5")
    floor6 = apartments.objects.filter(floor="6")
    floor7 = apartments.objects.filter(floor="7")
    floor8 = apartments.objects.filter(floor="8")
    floor9 = apartments.objects.filter(floor="9")
    floor10 = apartments.objects.filter(floor="10")
    floor11 = apartments.objects.filter(floor="11")
    floor12 = apartments.objects.filter(floor="12")
    floor13 = apartments.objects.filter(floor="13")
    floor14 = apartments.objects.filter(floor="14")
    floor15 = apartments.objects.filter(floor="15")
    floor16 = apartments.objects.filter(floor="16")

    commercial_floor_1 = commercial.objects.filter(floor="1")
    commercial_floor_2 = commercial.objects.filter(floor="2")

    context = {
        "floor3": floor3,
        "floor4": floor4,
        "floor5": floor5,
        "floor6": floor6,
        "floor7": floor7,
        "floor8": floor8,
        "floor9": floor9,
        "floor10": floor10,
        "floor11": floor11,
        "floor12": floor12,
        "floor13": floor13,
        "floor14": floor14,
        "floor15": floor15,
        "floor16": floor16,
        "parkings": parkings,
        "commercial_floor_1": commercial_floor_1,
        "commercial_floor_2": commercial_floor_2,
    }

    return render(request, "kv/base.html", context)


def building(request):
    return render(request, "kv/building.html")
