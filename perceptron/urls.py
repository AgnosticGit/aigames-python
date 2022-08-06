from django.urls import path

from perceptron.views.perceptron_view import load_perceptron


urlpatterns = [
    path('', load_perceptron)
]
