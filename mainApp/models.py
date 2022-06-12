from datetime import datetime
from django.db import models

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    salary = models.IntegerField()
    phone = models.IntegerField()
    role = models.CharField(max_length=30)
    hiredate = models.DateField()
    location = models.CharField(max_length=20,default=None,null=True,blank=True)

    # def __str__(self):      # __ first double underscore means -> its private and doesn't accesable ouside the class.
    #     return str(self.id)+" "+(self.name)+" "+(self.role)                   # __ last double underscore means -> same name se ek or built in h ye, if we dont call, the second one is call itself.
                            
     
