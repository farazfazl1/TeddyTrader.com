from django.shortcuts import render
from .models import Team
from teddyBears.models import TeddyBear


def home(req):
    team_data = Team.objects.all()
    teddy_bear_data = TeddyBear.objects.all()
    featured_teddy_bears = TeddyBear.objects.order_by(
        '-created_date').filter(is_featured=True)

    context = {
        'Team': team_data,
        'TeddyBear': teddy_bear_data,
        'Featured': featured_teddy_bears,
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
