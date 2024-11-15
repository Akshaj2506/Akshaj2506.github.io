from django.urls import path
from . import views

urlpatterns = [
   path("dashboard/", views.FlightDashboard, name="dashboard"),
   path('flight/add/', views.add_flight, name='add_flight'),  # Add flight
   path('flight/edit/<str:flight_number>/', views.edit_flight, name='edit_flight'),  # Edit flight
   path('flight/delete/<str:flight_number>/', views.delete_flight, name='delete_flight'),
]