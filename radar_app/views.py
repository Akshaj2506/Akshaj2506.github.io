from django.shortcuts import render, redirect, get_object_or_404
from .models import Flight
from datetime import datetime
from .forms import FlightForm
# Create your views here.
def FlightDashboard(request):
   currTime = datetime.now()
   flights = Flight.objects.all()

   for flight in flights:
      flight.calculate_progress(currTime)

   total_flights = Flight.objects.count()
   scheduled_flights = Flight.objects.filter(status="Scheduled").count()
   in_air_flights = Flight.objects.filter(status="In Progress").count()
   landed_flights = Flight.objects.filter(status="Completed").count()
   form = FlightForm()
   return render(request, "radar_app/dashboard.html", {
      "flights" : flights,
      "current_time" : currTime,
      "flight_count": total_flights,
      "scheduled_flight_count" : scheduled_flights,
      "in_air_flight_count": in_air_flights,
      "landed_flight_count" : landed_flights,
      "form" : form
   })

# Create Flight (CREATE operation)
def add_flight(request):
    if request.method == "POST":
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    return redirect('dashboard')

# Update Flight (UPDATE operation)
def edit_flight(request, flight_number):
    flight = get_object_or_404(Flight, flight_number=flight_number)
    if request.method == "POST":
        form = FlightForm(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    return redirect('dashboard')

# Delete Flight (DELETE operation)
def delete_flight(request, flight_number):
    flight = get_object_or_404(Flight, flight_number=flight_number)
    if request.method == "POST":
        flight.delete()
        return redirect('dashboard')
    return redirect('dashboard')