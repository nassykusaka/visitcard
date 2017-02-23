# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from mainapp.models import Work
from mainapp.models import Hobbies
from mainapp.models import Education
from mainapp.models import Work
from mainapp.models import Organization

class Command(BaseCommand):
    help = 'fill DB new data'
    def handle(self, *args, **options):
        hobbies = [
        {"name":"board games","year":"2000"},
        {"name":"longbording","year":"2014"},
        {"name":"movie-making","year":"2016"},
        {"name":"photo","year":"2010"},
        {"name":"snowbording","year":"2010"},
        {"name":"serfing","year":"2014"},
        {"name":"traveling","year":"2010"},
        {"name":"the other active types of sport","year":"2010"}]
        Hobbies.objects.all().delete()
        for hobbie in hobbies:
            hobbie = Hobbies(**hobbie)
            hobbie.save()
        schools = [{"sdate": "2005-09-01", "ldate": "2010-06-01", "name": "P.G. Demidov Yaroslavl State University","specialization": "Information technology in economic", "url": "http://www.uniyar.ac.ru/"},
                   {"sdate": "2014-04-25", "ldate": "2014-06-25", "name": "ISTQB", "specialization": "Foundation level", "url": "http://www.istqb.org/"},
                   {"sdate": "2016-10-01", "ldate": "2017-02-25", "name": "Code school", "specialization": "Django","url": "https://geekbrains.ru/"},
                   {"sdate": "2016-11-25", "ldate": "2017-03-25", "name":"GeekBrains", "specialization": "Programmer Python", "url": "http://127.0.0.1:8000/www.codeschool.com"}
                   ]
        Education.objects.all().delete()
        for school in schools:
            school = Education(**school)
            school.save()

        works = [
            {"organization": "NET ZONE","position": "Administrator in internet cafe","period": "09.2008 - 04.2009","responsibilities":"продажа и предоставление доступа в интернет для клиентов, помощь по всем вопросам"},
            {"organization": "Sunny bright","position": "test engineer","period": "06.2010 - 11.2010",
      "responsibilities":"Тестирование системы документообота для сетей отелей на базе продуктов Rational IBM"},
            {"organization": "MultiTop","position": "test engineer","period": "12.2010 - 11.2011","responsibilities":"Тестирование веб-портала с мультимедийным контентом, системой патентования,биллинговой системой"},
            {"organization": "Skyross technology","position": "test engineer","period": "11.2011 - 01.2012",
      "responsibilities":"Тестирование требований, систем видеонаблюдения,плат видео захвата, подготовка и сборка стендов, работа с hardware, постановка и анализ результатов нагрузочных тестов"},
            {"organization": "Lesta studio","position": "Senior lead of content QA group",
      "period": "02.2012 - 09.2016","responsibilities":"Организация процесса тестирования игровой функциональности (постановка цели, контроль качества выполнения, отчетность), создание, ревью и поддержка тестовой документации,участие в планировании разработки"}
        ]
        organizations = [
            {"name": "Lesta studio", "adress": "Saint Petersburg Obukhovskoy oborony pr. builing 70A buisness center Fidel", "phone_number": " + 7 (812) 320-84-45", "area": "game development", "region": "spb"},
            {"name": "Skyross technology", "adress": "SPb Remeslennaya st. 17", "phone_number": "+7 812 448-10-00", "area": "software for video monitoring", "region": "spb"},
            {"name": "Top Voiting technology(MultiTop)", "adress": "", "phone_number": "", "area": "web technology", "region": "spb"},
            {"name": "Sunny bright", "adress": "", "phone_number": "", "area": "soft for work flow", "region": "spb"},
            {"name": "NET ZONE", "adress": "Yaroslavl city Sovetskaya st. 11", "phone_number": "", "area": "internet cafe", "region": "Yaroslavskaya country"}
        ]
        for organization in organizations:
            organization = Organization(**organization)
            organization.save()
        for work in works:
            organization = work["organization"]
            # Получаем организацию по имени
            organization = Organization.objects.get(name=organization)
            # Заменяем название организации объектом
            work['organization'] = organization
            work = Work(**work)
            work.save()