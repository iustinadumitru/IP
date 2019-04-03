from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'Home.html'

class LoginView(TemplateView):
    template_name = 'Login.html'

class CinemaRoomsView(TemplateView):
    template_name = 'Cinema-Rooms.html'

class ForgotPasswordView(TemplateView):
	template_name = 'ForgotPassword.html'

class MoviesView(TemplateView):
	template_name = 'Movies.html'

class ProgramView(TemplateView):
	template_name = 'Program.html'

class RoomView(TemplateView):
	template_name = 'Room.html'

class SettingsView(TemplateView):
	template_name = 'Settings.html'

class SignUpView(TemplateView):
	template_name = 'SignUp.html'

class StatisticsView(TemplateView):
	template_name = 'Statistics.html'