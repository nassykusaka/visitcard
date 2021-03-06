# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response,Http404, get_object_or_404, loader
from .models import Work
from .models import Hobbies
from .models import Education
from .models import Organization
import datetime


def index(request):
    first_name = 'Anastasia'
    last_name = 'Chernyshova'
    birth = datetime.date(day=19, month=1, year=1989)
    place_of_birth = 'Naberezhnye Chelny'
    hobbies = Hobbies.objects.all()
    return render_to_response("index.html", {'hobbies': hobbies, 'first_name': first_name,
                                             'last_name': last_name, 'birth': birth, 'place_of_birth': place_of_birth})


def edu(request):
    schools = Education.objects.all()
    return render_to_response('education.html', {'schools': schools})


class School:
    def __init__(self, sdate, ldate, name, specialization, url):
        self.sdate = sdate
        self.ldate = ldate
        self.name = name
        self.specialization = specialization
        self.url = url


def work(request):
    works = Work.objects.all()
    return render_to_response('work.html', {'works': works})


def org(request, id):
    org = get_object_or_404(Organization, id=id)
    return render_to_response('org.html', {'organization': org})
