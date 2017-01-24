# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from .models import Work
from .models import Hobbies
from .models import Education
from django.contrib.auth.models import User

def index(request):
    first_name = 'Анастасия'
    last_name = 'Чернышова'
    birth = '19.01.1989'
    place_of_birth = 'Набережные Челны'
    #hobbies = ['сноуборд', 'серфинг', 'лонгборд', 'другие активные виды спорта', 'путешествия', 'фотография', 'видео-монтаж']
    hobbies = Hobbies.objects.all()
    return render_to_response("index.html", {'hobbies':hobbies, 'first_name':first_name,
                                             'last_name':last_name, 'birth':birth, 'place_of_birth': place_of_birth})

#class Work:
#    def __init__(self, organization, position, period, responsibilities):
#        self.organization = organization
#        self.position = position
#        self.period = period
#        self.responsibilities = responsibilities

def work(request):
    works = Work.objects.all()
    return render_to_response('work.html', {'works': works})

def edu(request):
    schools = Education.objects.all()
    return render_to_response('education.html', {'schools': schools})
class School:
    def __init__(self, period, name, specialization, url):
        self.period = period
        self.name = name
        self.specialization = specialization
        self.url = url