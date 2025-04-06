from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('company/', views.company, name='company'),
    path('service/', views.service, name='service'),
    path('products/dozimetry/', views.dozimetry, name='dozimetry'),
    path('products/radiometry/', views.radiometry, name='radiometry'),
    path('news/', views.news_list, name='news'),
    path('contact-request/', views.contact_request, name='contact_request'),
]
