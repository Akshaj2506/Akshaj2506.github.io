from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from radar_app.models import Flight
class Command(BaseCommand):
   help = "Creates a flight schedule and saves it on the database"
   
   def handle(self, *args, **kwargs):
      Flight.objects.all().delete()

      airline_info = {
         "Air India": {
            "iata_code": "AI",
            "destinations": [
                  {"destination": "New York (JFK)", "duration": "15:30"},
                  {"destination": "London (LHR)", "duration": "09:30"},
                  {"destination": "Dubai (DXB)", "duration": "03:45"},
                  {"destination": "Singapore (SIN)", "duration": "05:30"},
                  {"destination": "Sydney (SYD)", "duration": "12:15"},
                  {"destination": "Hong Kong (HKG)", "duration": "05:00"}
            ]
         },
         "IndiGo": {
            "iata_code": "6E",
            "destinations": [
                  {"destination": "Mumbai (BOM)", "duration": "02:10"},
                  {"destination": "Bengaluru (BLR)", "duration": "02:50"},
                  {"destination": "Chennai (MAA)", "duration": "02:35"},
                  {"destination": "Goa (GOI)", "duration": "02:30"},
                  {"destination": "Kolkata (CCU)", "duration": "02:15"},
                  {"destination": "Jaipur (JAI)", "duration": "01:15"}
            ]
         },
         "Vistara": {
            "iata_code": "UK",
            "destinations": [
                  {"destination": "London (LHR)", "duration": "09:20"},
                  {"destination": "Dubai (DXB)", "duration": "03:50"},
                  {"destination": "Singapore (SIN)", "duration": "05:20"},
                  {"destination": "Bengaluru (BLR)", "duration": "02:45"},
                  {"destination": "Kolkata (CCU)", "duration": "02:10"},
                  {"destination": "Mumbai (BOM)", "duration": "02:00"}
            ]
         },
         "SpiceJet": {
            "iata_code": "SG",
            "destinations": [
                  {"destination": "Dubai (DXB)", "duration": "03:50"},
                  {"destination": "Kolkata (CCU)", "duration": "02:15"},
                  {"destination": "Chennai (MAA)", "duration": "02:35"},
                  {"destination": "Goa (GOI)", "duration": "02:30"},
                  {"destination": "Bengaluru (BLR)", "duration": "02:50"},
                  {"destination": "Ahmedabad (AMD)", "duration": "01:45"}
            ]
         },
         "AirAsia India": {
            "iata_code": "I5",
            "destinations": [
                  {"destination": "Kuala Lumpur (KUL)", "duration": "05:00"},
                  {"destination": "Bengaluru (BLR)", "duration": "02:50"},
                  {"destination": "Mumbai (BOM)", "duration": "02:10"},
                  {"destination": "Chennai (MAA)", "duration": "02:35"},
                  {"destination": "Hyderabad (HYD)", "duration": "02:00"},
                  {"destination": "Kolkata (CCU)", "duration": "02:15"}
            ]
         },
         "Alliance Air": {
            "iata_code": "9I",
            "destinations": [
                  {"destination": "Bhopal (BHO)", "duration": "01:40"},
                  {"destination": "Shimla (SLV)", "duration": "01:20"},
                  {"destination": "Jammu (IXJ)", "duration": "01:25"},
                  {"destination": "Leh (IXL)", "duration": "01:45"},
                  {"destination": "Indore (IDR)", "duration": "01:50"},
                  {"destination": "Udaipur (UDR)", "duration": "01:40"}
            ]
         },
         "Air India Express": {
            "iata_code": "IX",
            "destinations": [
                  {"destination": "Dubai (DXB)", "duration": "03:50"},
                  {"destination": "Sharjah (SHJ)", "duration": "03:40"},
                  {"destination": "Abu Dhabi (AUH)", "duration": "03:45"},
                  {"destination": "Kochi (COK)", "duration": "03:00"},
                  {"destination": "Bengaluru (BLR)", "duration": "02:50"},
                  {"destination": "Chennai (MAA)", "duration": "02:35"}
            ]
         },
         "Emirates": {
            "iata_code": "EK",
            "destinations": [
                  {"destination": "Dubai (DXB)", "duration": "03:45"},
                  {"destination": "London (LHR)", "duration": "09:30"},
                  {"destination": "New York (JFK)", "duration": "15:30"},
                  {"destination": "Sydney (SYD)", "duration": "12:00"},
                  {"destination": "Singapore (SIN)", "duration": "05:20"},
                  {"destination": "Mumbai (BOM)", "duration": "02:10"}
            ]
         },
         "Qatar Airways": {
            "iata_code": "QR",
            "destinations": [
                  {"destination": "Doha (DOH)", "duration": "04:10"},
                  {"destination": "London (LHR)", "duration": "09:20"},
                  {"destination": "Paris (CDG)", "duration": "09:10"},
                  {"destination": "New York (JFK)", "duration": "15:20"},
                  {"destination": "Singapore (SIN)", "duration": "05:10"},
                  {"destination": "Kuala Lumpur (KUL)", "duration": "05:00"}
            ]
         },
         "Etihad Airways": {
            "iata_code": "EY",
            "destinations": [
                  {"destination": "Abu Dhabi (AUH)", "duration": "03:45"},
                  {"destination": "London (LHR)", "duration": "09:20"},
                  {"destination": "New York (JFK)", "duration": "15:30"},
                  {"destination": "Paris (CDG)", "duration": "09:15"},
                  {"destination": "Singapore (SIN)", "duration": "05:10"},
                  {"destination": "Sydney (SYD)", "duration": "12:00"}
            ]
         },
         "Singapore Airlines": {
            "iata_code": "SQ",
            "destinations": [
                  {"destination": "Singapore (SIN)", "duration": "05:30"},
                  {"destination": "London (LHR)", "duration": "09:20"},
                  {"destination": "New York (JFK)", "duration": "15:30"},
                  {"destination": "Paris (CDG)", "duration": "09:10"},
                  {"destination": "Sydney (SYD)", "duration": "12:10"},
                  {"destination": "Frankfurt (FRA)", "duration": "09:00"}
            ]
         },
         "British Airways": {
            "iata_code": "BA",
            "destinations": [
                  {"destination": "London (LHR)", "duration": "09:20"},
                  {"destination": "New York (JFK)", "duration": "15:30"},
                  {"destination": "Chicago (ORD)", "duration": "15:00"},
                  {"destination": "Los Angeles (LAX)", "duration": "17:00"},
                  {"destination": "Paris (CDG)", "duration": "09:10"},
                  {"destination": "Dubai (DXB)", "duration": "03:45"}
            ]
         },
         "Lufthansa": {
            "iata_code": "LH",
            "destinations": [
                  {"destination": "Frankfurt (FRA)", "duration": "08:50"},
                  {"destination": "Munich (MUC)", "duration": "09:00"},
                  {"destination": "New York (JFK)", "duration": "15:10"},
                  {"destination": "London (LHR)", "duration": "09:20"},
                  {"destination": "Singapore (SIN)", "duration": "05:30"},
                  {"destination": "Zurich (ZRH)", "duration": "09:00"}
            ]
         },
         "Thai Airways": {
            "iata_code": "TG",
            "destinations": [
                  {"destination": "Bangkok (BKK)", "duration": "04:00"},
                  {"destination": "Phuket (HKT)", "duration": "04:30"},
                  {"destination": "Singapore (SIN)", "duration": "05:00"},
                  {"destination": "Tokyo (NRT)", "duration": "07:00"},
                  {"destination": "Seoul (ICN)", "duration": "06:50"},
                  {"destination": "Hong Kong (HKG)", "duration": "05:00"}
            ]
         },
         "Cathay Pacific": {
            "iata_code": "CX",
            "destinations": [
                  {"destination": "Hong Kong (HKG)", "duration": "05:00"},
                  {"destination": "Los Angeles (LAX)", "duration": "16:30"},
                  {"destination": "New York (JFK)", "duration": "15:20"},
                  {"destination": "Tokyo (NRT)", "duration": "07:10"},
                  {"destination": "Singapore (SIN)", "duration": "05:00"},
                  {"destination": "Bangkok (BKK)", "duration": "04:30"}
            ]
         },
         "Turkish Airlines": {
            "iata_code": "TK",
            "destinations": [
                  {"destination": "Istanbul (IST)", "duration": "07:10"},
                  {"destination": "Paris (CDG)", "duration": "09:15"},
                  {"destination": "New York (JFK)", "duration": "15:20"},
                  {"destination": "London (LHR)", "duration": "09:20"},
                  {"destination": "Frankfurt (FRA)", "duration": "08:50"},
                  {"destination": "Dubai (DXB)", "duration": "03:45"}
            ]
         },
         "Malaysia Airlines": {
            "iata_code": "MH",
            "destinations": [
                  {"destination": "Kuala Lumpur (KUL)", "duration": "05:00"},
                  {"destination": "Sydney (SYD)", "duration": "12:00"},
                  {"destination": "Melbourne (MEL)", "duration": "12:10"},
                  {"destination": "Bangkok (BKK)", "duration": "04:00"},
                  {"destination": "Singapore (SIN)", "duration": "05:30"},
                  {"destination": "Hong Kong (HKG)", "duration": "05:00"}
            ]
         },
         "Japan Airlines": {
            "iata_code": "JL",
            "destinations": [
                  {"destination": "Tokyo (NRT)", "duration": "07:10"},
                  {"destination": "Osaka (KIX)", "duration": "07:00"},
                  {"destination": "New York (JFK)", "duration": "15:30"},
                  {"destination": "San Francisco (SFO)", "duration": "16:30"},
                  {"destination": "Los Angeles (LAX)", "duration": "16:40"},
                  {"destination": "Singapore (SIN)", "duration": "05:00"}
            ]
         },
         "SriLankan Airlines": {
            "iata_code": "UL",
            "destinations": [
                  {"destination": "Colombo (CMB)", "duration": "03:35"},
                  {"destination": "Singapore (SIN)", "duration": "05:00"},
                  {"destination": "Bangkok (BKK)", "duration": "04:00"},
                  {"destination": "Kuala Lumpur (KUL)", "duration": "05:10"},
                  {"destination": "Male (MLE)", "duration": "03:30"},
                  {"destination": "Hong Kong (HKG)", "duration": "05:00"}
            ]
         },
         "American Airlines": {
            "iata_code": "AA",
            "destinations": [
                  {"destination": "New York (JFK)", "duration": "15:30"},
                  {"destination": "Chicago (ORD)", "duration": "15:10"},
                  {"destination": "Dallas (DFW)", "duration": "16:00"},
                  {"destination": "Miami (MIA)", "duration": "16:20"},
                  {"destination": "Los Angeles (LAX)", "duration": "16:40"},
                  {"destination": "Philadelphia (PHL)", "duration": "15:20"}
            ]
         },
         "United Airlines": {
            "iata_code": "UA",
            "destinations": [
                  {"destination": "San Francisco (SFO)", "duration": "16:30"},
                  {"destination": "Chicago (ORD)", "duration": "15:10"},
                  {"destination": "Newark (EWR)", "duration": "15:20"},
                  {"destination": "Washington D.C. (IAD)", "duration": "15:40"},
                  {"destination": "Houston (IAH)", "duration": "16:00"},
                  {"destination": "Los Angeles (LAX)", "duration": "16:40"}
            ]
         },
         "China Eastern Airlines": {
            "iata_code": "MU",
            "destinations": [
                  {"destination": "Shanghai (PVG)", "duration": "06:00"},
                  {"destination": "Beijing (PEK)", "duration": "06:20"},
                  {"destination": "Guangzhou (CAN)", "duration": "06:40"},
                  {"destination": "Hong Kong (HKG)", "duration": "05:00"},
                  {"destination": "Tokyo (NRT)", "duration": "07:10"},
                  {"destination": "Bangkok (BKK)", "duration": "04:30"}
            ]
         },
         "KLM Royal Dutch Airlines": {
            "iata_code": "KL",
            "destinations": [
                  {"destination": "Amsterdam (AMS)", "duration": "08:40"},
                  {"destination": "Paris (CDG)", "duration": "09:10"},
                  {"destination": "London (LHR)", "duration": "09:20"},
                  {"destination": "Frankfurt (FRA)", "duration": "08:50"},
                  {"destination": "Dubai (DXB)", "duration": "03:45"},
                  {"destination": "Bangkok (BKK)", "duration": "04:30"}
            ]
         },
         "Air France": {
            "iata_code": "AF",
            "destinations": [
                  {"destination": "Paris (CDG)", "duration": "09:10"},
                  {"destination": "Amsterdam (AMS)", "duration": "08:40"},
                  {"destination": "Frankfurt (FRA)", "duration": "08:50"},
                  {"destination": "London (LHR)", "duration": "09:20"},
                  {"destination": "Dubai (DXB)", "duration": "03:45"},
                  {"destination": "Singapore (SIN)", "duration": "05:30"}
            ]
         },
      }

      start_time = datetime.strptime("00:00", "%H:%M")
      interval_minutes = 10
      num_flights = 144
      airline_keys = list(airline_info.keys())
      flight_counter = 100  # Starting flight number

      current_time = start_time
      for i in range(num_flights):
            airline_name = airline_keys[i % len(airline_keys)]
            airline_data = airline_info[airline_name]
            destination_info = airline_data["destinations"][i % len(airline_data["destinations"])]

            flight_number = f"{airline_data['iata_code']}{flight_counter + i}"

            # Save the flight to the database
            Flight.objects.create(
                departure_time=current_time.time(),
                airline=airline_name,
                iata_code=airline_data["iata_code"],
                flight_number=flight_number,
                destination=destination_info["destination"],
                duration=destination_info["duration"]
            )

            current_time += timedelta(minutes=interval_minutes)

      self.stdout.write(self.style.SUCCESS(f'Successfully created {num_flights} flights'))

