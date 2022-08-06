from django.contrib import admin
from django.contrib.sessions.models import Session
from perceptron.models import Perceptron

admin.site.register(Perceptron)
admin.site.register(Session)
