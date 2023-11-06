from django.core.exceptions import *
import re

#validation for characters only field
def validate(value):
   if  not value.isnumeric():
        return value
   else:
        print('Numberic')
        raise ValidationError("This field access only characters")
#validation for email field
def validate_email(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):  
        return email  
    else:
        raise ValidationError("Not valid Email")
    
 #validation for mobile number field   
def validate_mobile(value):
    if value.isnumeric() and len(value)==10:
        return value  
    else:
        raise ValidationError("This field have 10 digit and only numbers")

