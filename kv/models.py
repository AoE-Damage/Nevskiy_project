from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.
class apartments(models.Model):

    FLOORS = (
        ("3", "3 этаж"),
        ("4", "4 этаж"),
        ("5", "5 этаж"),
        ("6", "6 этаж"),
        ("7", "7 этаж"),
        ("8", "8 этаж"),
        ("9", "9 этаж"),
        ("10", "10 этаж"),
        ("11", "11 этаж"),
        ("12", "12 этаж"),
        ("13", "13 этаж"),
        ("14", "14 этаж"),
        ("15", "15 этаж"),
        ("16", "16 этаж"),
    )
    floor = models.CharField(max_length=2, choices=FLOORS)

    BEDROOMS = (("1", "1 комнатная"), ("2", "2 комнатная"), ("3", "3 комнатная"))
    number_of_bedrooms = models.CharField(max_length=1, choices=BEDROOMS)

    AREA = (
        ("46,5", "46,5"),
        ("43,5", "43,5"),
        ("49,2", "49,2"),
        ("43,8", "43,8"),
        ("72,1", "72,1"),
        ("72,4", "72,4"),
        ("100,1", "100,1"),
        ("93,2", "93,2"),
    )

    area = models.CharField(max_length=6, choices=AREA)

    AVAILABLE = (("yes", "Свободно"), ("no", "Занято"))
    available = models.CharField(max_length=3, choices=AVAILABLE)


class commercial(models.Model):
    FLOORS = (("1", "1 этаж"), ("2", "2 этаж"))

    floor = models.CharField(max_length=1, choices=FLOORS)

    AREA = (
        ("19,30", "19,30"),
        ("56,20", "56,20"),
        ("64,55", "64,55"),
        ("61,70", "61,70"),
        ("47,60", "47,60"),
        ("122,10", "122,10"),
        ("42,20", "42,20"),
        ("41,90", "41,90"),
        ("40,80", "40,80"),
        ("39,90 (1-L-sleva)", "39,90 (1) Слева"),
        ("39,90 (2-R-sprava)", "39,90 (2) Справа"),
        ("42,60", "42,60"),
        ("63 (1-L-sleva)", "63 (1) Слева"),
        ("63 (2-R-sprava)", "63 (2) Справа"),
        ("30,15", "30,15"),
        ("33,75", "33,75"),
    )

    area = models.CharField(max_length=25, choices=AREA)

    AVAILABLE = (("yes", "Свободно"), ("no", "Занято"))
    available = models.CharField(max_length=3, choices=AVAILABLE)


class zayavki(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=35)
    phone_number = models.CharField(max_length=13)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class parking(models.Model):

    SPOT = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("10", "10"),
        ("11", "11"),
        ("12", "12"),
        ("13", "13"),
        ("14", "14"),
        ("15", "15"),
        ("16", "16"),
        ("17", "17"),
        ("18", "18"),
        ("19", "19"),
        ("20", "20"),
        ("21", "21"),
        ("22", "22"),
        ("23", "23"),
        ("24", "24"),
        ("25", "25"),
        ("26", "26"),
        ("27", "27"),
        ("28", "28"),
        ("29", "29"),
    )

    spot = models.CharField(max_length=2, choices=SPOT)

    AVAILABLE = (("svobodno", "Свободно"), ("zanyato", "Занято"))
    available = models.CharField(max_length=10, choices=AVAILABLE)
