from django.shortcuts import render

def home(req):
    return render(req, 'pages/home.html')
