from django.shortcuts import render, redirect
from .models import Dozimetr, Radiometr, News
from .forms import RequestForm

def home(request):
    return render(request, 'products/home.html')

def company(request):
    return render(request, 'products/company.html')

def service(request):
    return render(request, 'products/service.html')

def dozimetry(request):
    dozimetry = Dozimetr.objects.all()
    return render(request, 'products/dozimetry.html', {'dozimetry': dozimetry})

def radiometry(request):
    radiometry = Radiometr.objects.all()
    return render(request, 'products/radiometry.html', {'radiometry': radiometry})


def news_list(request):
    news = News.objects.order_by('-created_at')
    return render(request, 'products/news.html', {'news': news})


def contact_request(request):
    submitted = False
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contact-request?submitted=True')
    else:
        form = RequestForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'products/contact_request.html', {'form': form, 'submitted': submitted})