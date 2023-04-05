from django.shortcuts import render
from .models import Team
from teddyBears.models import TeddyBear


def home(req):
    team_data = Team.objects.all()
    teddy_bear_data = TeddyBear.objects.all()
    featured_teddy_bears = TeddyBear.objects.order_by(
        '-created_date').filter(is_featured=True)

    # --search box field looks for those values and passes them to html
    brand_search = TeddyBear.objects.values_list(
        'brand', flat=True).distinct().order_by('brand')
    year_search = TeddyBear.objects.values_list(
        'year', flat=True).distinct().order_by('year')
    condition_search = TeddyBear.objects.values_list(
        'condition', flat=True).distinct().order_by('condition')
    tag_search = TeddyBear.objects.values_list(
        'tag', flat=True).distinct().order_by('tag')

    # Reset form fields to default values
    keyword = req.GET.get('keyword', '')
    brand = req.GET.get('brand', '')
    condition = req.GET.get('condition', '')
    tag = req.GET.get('tag', '')

    if not (keyword or brand or condition or tag):
        keyword = ''
        brand = ''
        condition = ''
        tag = ''

    context = {
        'Team': team_data,
        'TeddyBear': teddy_bear_data,
        'Featured': featured_teddy_bears,
        'brand_search': brand_search,
        'year_search': year_search,
        'condition_search': condition_search,
        'tag_search': tag_search,
        'keyword': keyword,
        'brand': brand,
        'condition': condition,
        'tag': tag,
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
