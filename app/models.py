from django.db import models

# Create your models here.
class Healthyheart_Users (models.Model):
    Patient_name = models.CharField(max_length = 150)
    Age = models.SmallIntegerField()
    Gender = models.CharField(max_length = 150)
    Chestpaintype = models.SmallIntegerField()
    RestBP =  models.SmallIntegerField()
    Cholestrol =  models.SmallIntegerField()
    Heartrate = models.SmallIntegerField()
    Exercise_induced_angina =  models.SmallIntegerField()
    Oldpeak = models.FloatField() 
    Slope = models.SmallIntegerField()
    No_of_vessels = models.SmallIntegerField()
    Thal = models.SmallIntegerField()
    Report_date = models.DateField()

    def __str__(self): 
         return self.Patient_name