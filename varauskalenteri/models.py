from django.db import models
import datetime

class Tapahtuma(models.Model):
    otsikko = models.CharField(max_length=200)
    kuvaus = models.TextField()
    alku = models.DateTimeField()
    loppu = models.DateTimeField()

    def __str__(self):
        return f"{self.otsikko} ({self.alku}--{self.loppu})"

    
            

    def kesto(self) -> datetime.timedelta:        
        return self.loppu - self.alku


    def kesto_tuntia(self):
        kesto = self.kesto()
        kesto.days
        return kesto.loppu - self.alku