from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Income(models.Model):
    income_text     = models.CharField(max_length=200)
    money_in_text   = models.CharField(max_length=20)
    expenses_text   = models.CharField(max_length=200)
    money_out_text  = models.CharField(max_length=20)
    remaining       = models.FloatField(default=0)
    pub_date        = models.DateTimeField('date published')
    
   
    def __str__(self):
        return self.income_text
        return self.money_in_text
        return self.expenses_text
        return self.money_in_text
       

