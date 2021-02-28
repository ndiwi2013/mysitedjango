from django.db import models

#creer votre models ici

class Customer(models
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)

def _str_(self):
    return self.first_name +' '+self.last_name