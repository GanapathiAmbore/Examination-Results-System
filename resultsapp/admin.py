from django.contrib import admin
from resultsapp.models import Halticket,Student
tables=[Halticket,Student]
admin.site.register(tables)
