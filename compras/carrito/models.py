from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime
import uuid

# Create your models here.
class ListProducts(models.Model): 
    id = models.AutoField(primary_key=True) 
    CATEGORY =(
        ('Verdura', 'Verdura'),
        ('Lacteo', 'Lacteo'),
        ('Fruta', 'Fruta'),
        ('Cereal', 'Cereal'),
        ('Carnes', 'Carnes'),
        ('Otro', 'Otro'), 
    )
    type = models.CharField(choices= CATEGORY, default='Otro', max_length=100, blank=True, help_text="tipo producto")
    product = models.CharField(max_length=200,name='product')   
    client = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    creation_date = models.DateField(null=True, blank=True, default=datetime.today)
    status_delete = models.BooleanField(default=False)

    def __str__(self):
        
        return '%s (%s)' % (self.product,self.creation_date) 

    def get_absolute_url(self): 
        return f"/products-list/{self.pk}" 