# pages/urls.py
from django.urls import path

from .views import *

urlpatterns = [
    path('Home.html', HomeView.as_view(), name='home'),
    path('Cinema-rooms.html', CinemaRoomsView.as_view(), name='cinemarooms'),
    path('Forgotpassword.html', ForgotPasswordView.as_view(), name='forgotpassword'),
    path('Login.html', LoginView.as_view(), name='login'),
    path('Movies.html', MoviesView.as_view(), name='movies'),
    path('Program.html', ProgramView.as_view(), name='program'),
    path('Room.html', RoomView.as_view(), name='room'),
    path('Settings.html', SettingsView.as_view(), name='settings'),
    path('Signup.html', SignUpView.as_view(), name='signup'),
    path('Statistics.html', StatisticsView.as_view(), name='statistics'),
]
