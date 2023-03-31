from django.shortcuts import render
from .models import Team


def home(req):
    team_data = Team.objects.all()

    context = {
        'Team': team_data
    }
    return render(req, 'pages/home.html', context)


def about(req):
    team_data = Team.objects.all()

    context = {
        'Team': team_data
    }

    return render(req, 'pages/about.html', context)


def contact(req):
    return render(req, 'pages/contact.html')


def services(req):
    return render(req, 'pages/services.html')
