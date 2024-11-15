from django import forms
from .models import Flight

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['departure_time', 'airline', 'iata_code', 'flight_number', 'destination', 'duration']
