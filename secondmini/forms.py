from django.forms import ModelForm
from django import forms
from django.core import validators
from .models import Booking,Doctors
from django.core.exceptions import ValidationError

import re
from .validators import *



class DateInput(forms.DateInput):
    input_type='date'

class BookingForm(forms.ModelForm):
    p_name=forms.CharField(max_length=255,validators=[validate])
    p_phone=forms.CharField(max_length=10,validators=[validate_mobile])
    p_email=forms.EmailField(validators=[validate_email])
    # doc_name=.ForeignKey(Doctors,on_delete=forms.CASCADE)
    # booking_date=forms.DateField()
    # booked_on=forms.DateField()
    
        

    class Meta:
        model=Booking
        fields=('doc_name','booking_date',)
 
        widgets = {
            'booking_date': DateInput()
        }
        
        labels={
            'p_name':"Patient Name ",
            'p_phone':"Patient Phone",
            'p_email':"Patient Email",
            'doc_name':"Doctor Name",
            'booking_date':"Booking Date"}
    # def clean(self):
    #     super(BookingForm,self).clean
       
    #     p_name=self.cleaned_data.get('p_name')

    #         # def validate(value):
    #     if  p_name.isnumeric():
    #         self._errors['p_name']=self.error_class(["This field access only characters"])
    #     return self.cleaned_data