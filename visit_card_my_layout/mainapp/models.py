# -*- coding: utf-8 -*-
from django.db import models


class Organization(models.Model):
    name = models.CharField(verbose_name='Organization name',max_length=32, unique=True)
    adress = models.CharField(verbose_name='Adress',max_length=32, blank=True)
    phone_number = models.CharField(verbose_name='Phone',max_length=32, blank=True)
    area = models.CharField(verbose_name='Area',max_length=32)
    region = models.CharField(verbose_name='Region',max_length=32)

    def __str__(self):
        return self.name


class Work(models.Model):
    organization = models.ForeignKey(Organization, verbose_name='Organization name')
    position = models.CharField(max_length=32)
    sdate = models.DateField(null=True)
    ldate = models.DateField(null=True)
    responsibilities = models.TextField()

    def __str__(self):
        return self.position


class Hobbies(models.Model):
    name = models.CharField(max_length=32, unique=True)
    year = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Education(models.Model):
    sdate = models.DateField(null=True)
    ldate = models.DateField(null=True)
    name = models.CharField(max_length=40)
    specialization = models.CharField(max_length=40)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name
