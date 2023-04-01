from django.shortcuts import render
from .models import TeddyBear


def home(req):
    return render(req, 'teddyBears/teddyBears.html')
