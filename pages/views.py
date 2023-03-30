from django.shortcuts import render


def home(req):
    return render(req, 'pages/home.html')


def about(req):
    return render(req, 'pages/about.html')


def contact(req):
    return render(req, 'pages/contact.html')


def services(req):
    return render(req, 'pages/services.html')
