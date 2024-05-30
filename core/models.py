from django.db import models
from datetime import datetime
# Create your models here.

class Expense(models.Model):
    category = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    date = models.DateField(auto_now=False)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.category} ({str(self.date)})"

class Income(models.Model):
    income = models.IntegerField(default=0)
    month = models.CharField(max_length=30,default=datetime.now().strftime('%m-%Y'), primary_key=True)

    def __str__(self):
        return f"{self.month} (${self.income})"

