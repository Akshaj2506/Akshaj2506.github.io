from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class Flight(models.Model):
    departure_time = models.TimeField()
    airline = models.CharField(max_length=100)
    iata_code = models.CharField(max_length=3)
    flight_number = models.CharField(max_length=10, unique=True)
    destination = models.CharField(max_length=100)
    duration = models.CharField(max_length=5)
    status = models.CharField(max_length=50, default="Scheduled")  # Scheduled, In-Flight, Landed
    progress = models.IntegerField(default=0)  # Progress percentage, 0-100

    def calculate_progress(self, current_time):
        """
        Calculates the progress percentage based on the departure time, duration,
        and the current time.
        """
        # Convert time and duration to datetime for calculation
        departure_dt = datetime.combine(datetime.today(), self.departure_time)
        duration_parts = self.duration.split(":")
        flight_duration = timedelta(hours=int(duration_parts[0]), minutes=int(duration_parts[1]))
        arrival_time = departure_dt + flight_duration

        # Calculate progress based on current time
        if current_time < departure_dt:
            self.status = "Scheduled"
            self.progress = 0
        elif current_time >= arrival_time:
            self.status = "Completed"
            self.progress = 100
        else:
            self.status = "In Progress"
            elapsed_time = current_time - departure_dt
            self.progress = min(100, int((elapsed_time.total_seconds() / flight_duration.total_seconds()) * 100))
        
        self.save()