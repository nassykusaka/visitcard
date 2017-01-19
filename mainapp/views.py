# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response

def index(request):
    first_name = 'Анастасия'
    last_name = 'Чернышова'
    birth = '19.01.1989'
    place_of_birth = 'Набережные Челны'
    hobbies = ['сноуборд', 'серфинг', 'лонгборд', 'другие активные виды спорта', 'путешествия', 'фотография', 'видео-монтаж']
    return render_to_response("index.html", {'hobbies':hobbies, 'first_name':first_name,
                                             'last_name':last_name, 'birth':birth, 'place_of_birth': place_of_birth})
def work(request):
       return render_to_response('work.html', {'works':works})

class Work:
    def __init__(self, organization, position, period, responsibilities):
        self.organization = organization
        self.position = position
        self.period = period
        self.responsibilities = responsibilities

works = [
    Work('NET ZONE', 'Администратор интернет кафе', '09.2008 - 04.2009','продажа и предоставление доступа в интернет для клиентов, помощь по всем вопросам'),
    Work('Sunny bright','Тестировщик', '06.2010 - 11.2010', 'Тестирование системы документообота для сетей отелей на базе продуктов Rational IBM'),
    Work('Старт-ап Мультитоп', 'Тестировщик', '12.2010 - 11.2011', 'Тестирование веб-портала с мультимедийным контентом, системой патентования,биллинговой системой'),
    Work('Скайрос технологии', 'Инженер по тестированию', '11.2011 - 01.2012', 'Тестирование требований, систем видеонаблюдения,плат видео захвата, подготовка и сборка стендов, работа с hardware, постановка и анализ результатов нагрузочных тестов'),
    Work('Lesta llc', 'Руководитель группы тестирования контента и внутреннего инструментария', '02.2012 - 09.2016', 'Организация процесса тестирования игровой функциональности (постановка цели, контроль качества выполнения, отчетность), создание, ревью и поддержка тестовой документации,участие в планировании разработки')
    ]

def edu(request):
    return render_to_response('education.html', {'schools': schools})
class School:
    def __init__(self, period, name, specialization, url):
        self.period = period
        self.name = name
        self.specialization = specialization
        self.url = url

schools = [
    School('2005 - 2010', 'Ярославский Государственный Университет им. П.Г.Демидова', 'Информатика в экономике', 'http://www.uniyar.ac.ru/'),
    School('2014', 'ISTQB', 'Foundation level', 'http://www.istqb.org/'),
    School('2016 - 2017', 'Geekbrains', 'Программист Python', 'https://geekbrains.ru')
]