from django.db import models
from django.core.exceptions import ValidationError
import re

# Create your models here.

#validation for characters only field
def validate(value):
   if  not value.isnumeric():
        return value
   else:
        raise ValidationError("This field access only characters")
   
#validation for email field
def validate_email(email):  
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):  
        return email  
    else:
        raise ValidationError("Not valid Email")
    
 #validation for mobile number field   
def validate_mobile(value):
    a=[1,0,2,3,4,5,6,7,8,9]
    if value in a and len(value)==10:
        return value  
    else:
        raise ValidationError("This field have 10 digit and only numbers")

 #create table for Departments   
class Departments(models.Model):
    dep_name=models.CharField(max_length=100,validators=[validate])
    dep_description=models.TextField()

    def __str__(self):
        return self.dep_name #access name for after use


class Doctors(models.Model):
    doc_name=models.CharField(max_length=255,validators=[validate])
    doc_spec=models.CharField(max_length=255,validators=[validate])
    dep_name=models.ForeignKey(Departments,on_delete=models.CASCADE)
    doc_img=models.ImageField(upload_to='doctors')

    def __str__(self):
        return 'Dr '+self.doc_name+'-('+self.doc_spec+')'



class Booking(models.Model):
    p_name=models.CharField(max_length=255)
    p_phone=models.CharField(max_length=10)
    p_email=models.EmailField()
    doc_name=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)
