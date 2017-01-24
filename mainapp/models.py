from django.db import models

class Work(models.Model):
    organization = models.CharField(max_length=32)
    position = models.CharField(max_length=32)
    period = models.CharField(max_length=32)
    #to do: split period for date_of_start and finish work
    responsibilities = models.TextField()
    def __str__(self):
        return self.organization

class Hobbies(models.Model):
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name

class Education(models.Model):
    period = models.CharField(max_length=32)
    #to do: split to start & end date
    name = models.CharField(max_length=32)
    specialization = models.CharField(max_length=32)
    url = models.CharField(max_length=64)
    def __str__(self):
        return self.name