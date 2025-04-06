from django.contrib import admin
from .models import Dozimetr, Radiometr, News, Request

admin.site.register(Dozimetr)
admin.site.register(Radiometr)
admin.site.register(News)
admin.site.register(Request)