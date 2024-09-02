from django import forms
from .models import Booking
class DateInput(forms.DateInput):
    input_type = 'date'
class Bookingform(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'

        widgets={
           'book_date':DateInput()
        }
        labels = {
            'cus_name':"Name:",
            'cus_phone':"Phone Number:",
            'cus_email':"E-mail:" ,
            'room_type':"Room type:",
             'book_date':"Booking Date:",

        }


