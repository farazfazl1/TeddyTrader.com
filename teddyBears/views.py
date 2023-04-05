from django.shortcuts import render, get_object_or_404
from .models import TeddyBear
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def home(req):
    teddybear_data = TeddyBear.objects.order_by('-created_date')
    paginator = Paginator(teddybear_data, 4)  # 1
    page = req.GET.get('page')  # 2
    paged_teddy_bears = paginator.get_page(page)  # 3

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
        'TeddyBear': paged_teddy_bears,
        'brand_search': brand_search,
        'year_search': year_search,
        'condition_search': condition_search,
        'tag_search': tag_search,
        'keyword': keyword,
        'brand': brand,
        'condition': condition,
        'tag': tag,
    }

    return render(req, 'teddyBears/teddyBears.html', context)


def teddybear(req, id):
    teddybear_info = get_object_or_404(TeddyBear, pk=id)

    context = {
        'TeddyBear': teddybear_info
    }

    return render(req, 'teddyBears/tbDetails.html', context)


def search(req):
    teddybear_data = TeddyBear.objects.order_by('-created_date')

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

    if 'keyword' in req.GET:  # if we have a keyword name in url
        # we store keyword's given valuye in keyword variable
        keyword = req.GET['keyword']
        if keyword:
            teddybear_data = teddybear_data.filter(
                description__icontains=keyword)

    if 'brand' in req.GET:  # if we have a keyword name in url
        # we store keyword's given valuye in keyword variable
        brand = req.GET['brand']
        if brand:
            teddybear_data = teddybear_data.filter(
                brand__iexact=brand)  # checking it for exact value instead of looking for similar in description

    if 'year' in req.GET:  # if we have a keyword name in url
        # we store keyword's given valuye in keyword variable
        year = req.GET['year']
        if year:
            teddybear_data = teddybear_data.filter(
                year__iexact=year)  # checking it for exact value instead of looking for similar in description

    if 'condition' in req.GET:  # if we have a keyword name in url
        # we store keyword's given valuye in keyword variable
        condition = req.GET['condition']
        if condition:
            teddybear_data = teddybear_data.filter(
                condition__iexact=condition)  # checking it for exact value instead of looking for similar in description

    if 'tag' in req.GET:  # if we have a keyword name in url
        # we store keyword's given valuye in keyword variable
        tag = req.GET['tag']
        if tag:
            teddybear_data = teddybear_data.filter(
                tag__iexact=tag)  # checking it for exact value instead of looking for similar in description

    if 'min_price' in req.GET:
        min_price = req.GET['min_price']
        max_price = req.GET['max_price']
        if max_price:
            teddybear_data = teddybear_data.filter(
                price__gte=min_price, price__lte=max_price)
            # this means price is >= minimum price and <= maximum price
            
    context = {
        'TeddyBear': teddybear_data,
        'brand_search': brand_search,
        'year_search': year_search,
        'condition_search': condition_search,
        'tag_search': tag_search,
        'keyword': keyword,
        'brand': brand,
        'condition': condition,
        'tag': tag,
    }

    return render(req, 'teddyBears/search.html', context)
