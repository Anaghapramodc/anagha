from django.db import models

# Create your models here.

class product(models.Model):
    name=models.CharField(max_length=250)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    description=models.CharField(max_length=500)


#ORM Queries
"""
tablename.objects.all()
tablename.objects.all().values()
tablename.objects.get(id=1)
delete()
save()
"""

